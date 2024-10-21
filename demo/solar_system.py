import pygame
import random
import math

# Initialize Pygame
pygame.init()

### CONFIGURABLE PARAMETERS ###

# Screen dimensions
WIDTH, HEIGHT = 1200, 800

# Simulation parameters
NUM_PARTICLES = 200        # Number of particles
TIME_STEP = 1              # Time step for the simulation
G = 6.67430e-2             # Gravitational constant (scaled for simulation)
PARTICLE_MASS_MIN = 1      # Minimum mass of particles
PARTICLE_MASS_MAX = 10     # Maximum mass of particles
DISTANCE_MIN = 200         # Minimum initial distance from the sun
DISTANCE_MAX = 600         # Maximum initial distance from the sun
SUN_MASS = 20000           # Mass of the sun
SUN_RADIUS = 20            # Radius of the sun
TRAIL_LENGTH = 50          # Length of the particle trails
DAMPING_FACTOR = 1         # Damping factor (set to 1 for no damping)

# Colors
COLOR_BACKGROUND = (45, 45, 45)      # Dark Grey
COLOR_WHITE = (255, 255, 255)
COLOR_SUN = (235, 195, 50)
COLOR_SUN_OUTLINE = (240, 195, 195)  # Outline for the sun

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simplified Solar System Formation Simulation")

# Clock to control the frame rate
clock = pygame.time.Clock()

def get_particle_color(mass):
    """Assign a color based on the particle's mass."""
    if mass < 5:
        return (50, 215, 200)  # Turquoise
    elif mass < 10:
        return (30, 100, 100)  # Dark Teal
    elif mass < 15:
        return (240, 95, 95)   # Red Orange
    else:
        return (125, 45, 45)   # Dark Red

class Particle:
    """Class to represent particles in the simulation."""
    def __init__(self, x, y, mass, vx=0, vy=0, color=COLOR_WHITE, is_sun=False):
        self.x = x                      # X position
        self.y = y                      # Y position
        self.mass = mass                # Mass of the particle
        self.radius = max(2, int(self.mass ** 0.5))  # Radius based on mass
        self.vx = vx                    # X velocity
        self.vy = vy                    # Y velocity
        self.color = color              # Color for drawing
        self.is_sun = is_sun            # Flag to indicate if this is the sun
        self.trail = []                 # List to store positions for trail

    def update(self):
        """Update the particle's position based on its velocity."""
        # Apply damping to velocities
        self.vx *= DAMPING_FACTOR
        self.vy *= DAMPING_FACTOR

        self.x += self.vx * TIME_STEP
        self.y += self.vy * TIME_STEP

        # Append current position to trail
        self.trail.append((self.x, self.y))
        if len(self.trail) > TRAIL_LENGTH:
            self.trail.pop(0)

    def draw(self, screen, center_x, center_y, scale):
        """Draw the particle and its trail on the screen."""
        # Adjust positions based on center and scale
        draw_x = int((self.x - center_x) * scale + WIDTH / 2)
        draw_y = int((self.y - center_y) * scale + HEIGHT / 2)
        draw_radius = max(1, int(self.radius * scale))

        # Draw the trail
        if len(self.trail) > 1:
            trail_points = [
                (
                    int((pos[0] - center_x) * scale + WIDTH / 2),
                    int((pos[1] - center_y) * scale + HEIGHT / 2)
                )
                for pos in self.trail
            ]
            pygame.draw.lines(screen, self.color, False, trail_points, 1)

        # Draw the particle
        pygame.draw.circle(screen, self.color, (draw_x, draw_y), draw_radius)

        # Draw outline if it's the sun
        if self.is_sun:
            outline_radius = draw_radius + 3  # Thickness of the outline
            pygame.draw.circle(screen, COLOR_SUN_OUTLINE, (draw_x, draw_y), outline_radius, 1)  # Outline with thickness=1

def create_particles(num_particles, sun):
    """Generate particles orbiting around the central sun."""
    particles = [sun]
    for _ in range(num_particles):
        # Random distance and angle from the sun
        distance = random.uniform(DISTANCE_MIN, DISTANCE_MAX)
        angle = random.uniform(0, 2 * math.pi)
        x = sun.x + distance * math.cos(angle)
        y = sun.y + distance * math.sin(angle)

        # Random mass
        mass = random.uniform(PARTICLE_MASS_MIN, PARTICLE_MASS_MAX)

        # Assign color based on mass
        color = get_particle_color(mass)

        # Calculate initial velocity for a stable orbit
        speed = math.sqrt(G * sun.mass / distance)
        direction = angle + math.pi / 2  # Perpendicular to radius vector
        vx = speed * math.cos(direction)
        vy = speed * math.sin(direction)

        particle = Particle(x, y, mass, vx, vy, color)
        particles.append(particle)
    return particles

def calculate_forces(particles):
    """Calculate gravitational forces between particles (optimized)."""
    for i in range(len(particles)):
        p1 = particles[i]
        for j in range(i + 1, len(particles)):
            p2 = particles[j]
            dx = p2.x - p1.x
            dy = p2.y - p1.y
            distance = math.hypot(dx, dy)
            if distance > 0:
                # Gravitational force magnitude
                force = G * p1.mass * p2.mass / distance ** 2
                # Components of the force
                fx = force * dx / distance
                fy = force * dy / distance
                # Update velocities based on force (equal and opposite)
                p1.vx += (fx / p1.mass) * TIME_STEP
                p1.vy += (fy / p1.mass) * TIME_STEP
                p2.vx -= (fx / p2.mass) * TIME_STEP
                p2.vy -= (fy / p2.mass) * TIME_STEP

def handle_collisions(particles, sun):
    """Merge particles that collide, conserving angular momentum."""
    to_remove = set()
    num_particles = len(particles)
    for i in range(num_particles):
        p1 = particles[i]
        if p1 in to_remove:
            continue
        for j in range(i + 1, num_particles):
            p2 = particles[j]
            if p2 in to_remove:
                continue
            dx = p2.x - p1.x
            dy = p2.y - p1.y
            distance = math.hypot(dx, dy)
            if distance < p1.radius + p2.radius:
                # Check if either particle is the sun
                if p1.is_sun or p2.is_sun:
                    # Identify the non-sun particle
                    non_sun = p2 if p1.is_sun else p1
                    # Remove the non-sun particle
                    to_remove.add(non_sun)
                    continue  # Skip merging

                # Determine which particle is larger
                if p1.mass >= p2.mass:
                    larger, smaller = p1, p2
                else:
                    larger, smaller = p2, p1

                # --- Angular Momentum Conservation ---

                # Total mass
                total_mass = larger.mass + smaller.mass

                # Center of mass velocity (momentum conservation)
                vx_cm = (larger.vx * larger.mass + smaller.vx * smaller.mass) / total_mass
                vy_cm = (larger.vy * larger.mass + smaller.vy * smaller.mass) / total_mass

                # Update larger particle
                larger.mass = total_mass
                larger.radius = max(2, int(larger.mass ** 0.5))  # Update radius based on new mass
                larger.vx = vx_cm
                larger.vy = vy_cm

                # Assign new color based on updated mass
                larger.color = get_particle_color(larger.mass)

                # Combine trails
                larger.trail.extend(smaller.trail)
                larger.trail = larger.trail[-TRAIL_LENGTH:]

                # Remove smaller particle
                to_remove.add(smaller)
    # Remove merged particles
    particles[:] = [p for p in particles if p not in to_remove]

def main():
    """Main function to run the simulation."""
    # Create central mass (Sun) with is_sun=True
    sun = Particle(0, 0, SUN_MASS, color=COLOR_SUN, is_sun=True)
    sun.radius = SUN_RADIUS

    # Create particles
    particles = create_particles(NUM_PARTICLES, sun)

    # Simulation parameters
    center_x, center_y = 0, 0  # Center of the view (in simulation coordinates)
    scale = 1.0                # Zoom scale factor

    # Simulation loop
    running = True
    while running:
        clock.tick(60)  # Limit to 60 frames per second
        screen.fill(COLOR_BACKGROUND)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Zoom in and out with up and down arrow keys
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    scale *= 1.1  # Zoom in
                elif event.key == pygame.K_DOWN:
                    scale /= 1.1  # Zoom out

        # Calculate forces and update particle velocities
        calculate_forces(particles)

        # Update positions and handle collisions
        for particle in particles:
            particle.update()
        handle_collisions(particles, sun)

        # Draw particles
        for particle in particles:
            particle.draw(screen, center_x, center_y, scale)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
