import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)
        if velocity is None:
            angle = random.uniform(0, 360)
            speed = random.uniform(50, 150)
            self.velocity = pygame.math.Vector2(speed, 0).rotate(angle)
        else: 
            self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        else:
            log_event("asteroid_split")
            new_radius = self.radius / 2 
            if new_radius < ASTEROID_MIN_RADIUS:
                new_radius = ASTEROID_MIN_RADIUS

            # Handling new asteroids from split
            new_asteroids = []
            for _ in range(2):
                angle_offset = random.uniform(-30, 30) 
                new_velocity = self.velocity.rotate(angle_offset) * 1.2 
                offset_distance = self.radius + new_radius
                new_position = self.position + new_velocity.normalize() * offset_distance
                new_asteroids.append(Asteroid(new_position.x, new_position.y, new_radius, new_velocity))
            return new_asteroids


