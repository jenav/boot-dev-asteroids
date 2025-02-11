from circleshape import *
from constants import *


class Shot(CircleShape):
    def __init__(self, pos_vector):
        super().__init__(pos_vector.x, pos_vector.y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, SHOT_COLOR, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.should_kill_myself()
