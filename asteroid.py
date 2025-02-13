import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    asteroid_images = [None, None, None]

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        img_index = (radius // ASTEROID_MIN_RADIUS) - 1

        if not Asteroid.asteroid_images[img_index]:
            Asteroid.asteroid_images[img_index] = pygame.image.load(
                f"images/asteroid-{img_index}.png"
            ).convert_alpha()

        self.img = Asteroid.asteroid_images[img_index]

    def draw(self, screen):
        # pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        screen.blit(
            self.img, (self.position.x - self.radius, self.position.y - self.radius)
        )

    def update(self, dt):
        self.position += self.velocity * dt
        self.should_kill_myself()

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vel_angled_1 = self.velocity.rotate(random_angle)
        vel_angled_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = vel_angled_1 * 1.2
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = vel_angled_2 * 1.2
