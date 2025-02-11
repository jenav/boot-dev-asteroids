import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        if radius == ASTEROID_MAX_RADIUS:
            self.img = pygame.image.load("img/big-circle.png").convert_alpha()
        elif radius == (ASTEROID_MAX_RADIUS - ASTEROID_MIN_RADIUS):
            self.img = pygame.image.load("img/medium-circle.png").convert_alpha()
        else:
            self.img = pygame.image.load("img/small-circle.png").convert_alpha()

        super().__init__(x, y, radius)

    def draw(self, screen):
        # pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        screen.blit(
            self.img,
            (self.position.x - self.radius, self.position.y - self.radius),
        )
        pygame.draw.circle(screen, (200, 200, 200), self.position, self.radius, 1)

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
