import random
from constants import *
from circleshape import *
from shot import *
from lives import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_count = 0
        self.shoot_timer = 0
        self.shoot_sound = pygame.mixer.Sound("sounds/por.mp3")
        self.shoot_sound.set_volume(0.6)
        self.hit_sound = pygame.mixer.Sound("sounds/hit.mp3")
        self.lives = Lives()
        self.color = PLAYER_COLORS[self.lives.get_lives() - 1]

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.triangle(), 2)

    def draw_lives(self, screen):
        self.lives.draw(screen)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.shoot_timer -= dt
        if self.shoot_timer < 0:
            self.shoot_timer = 0

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return

        self.shoot_count += 1
        if self.shoot_count % random.randint(18, 60) == 0:
            self.shoot_sound.play()
            self.shoot_count = 0

        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.triangle()[0], self.color)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def set_color(self):
        self.color = PLAYER_COLORS[self.lives.get_lives() - 1]

    def get_hit(self):
        self.hit_sound.play()
        self.lives.akshually()
        self.set_color()

    def is_alive(self):
        return self.lives.get_lives() > 0
