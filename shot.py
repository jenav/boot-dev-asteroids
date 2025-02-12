from circleshape import *
from constants import *


class Shot(CircleShape):
    def __init__(self, pos_vector, color):
        super().__init__(pos_vector.x, pos_vector.y, BULLET_RADIUS)
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.should_kill_myself()
