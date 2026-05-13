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

    def split_on_collision(self, other_asteroid):
        self.kill() # This asteroid is the one being "split" and removed

        if self.radius <= ASTEROID_MIN_RADIUS:
            return [] # Cannot split further, so return empty list

        log_event("asteroid_collision_split")
        new_asteroids = []
        new_radius = self.radius / 2 # Halve the radius, or reduce by a fixed amount
        if new_radius < ASTEROID_MIN_RADIUS:
            new_radius = ASTEROID_MIN_RADIUS

        # Calculate direction from 'other_asteroid' to 'self'
        direction_vector = (self.position - other_asteroid.position).normalize()

        # Split into two new asteroids
        for _ in range(2):
            # New asteroids appear "about 1 mid sized asteroid away" from the collision site.
            # Let's use ASTEROID_MIN_RADIUS as the "mid-sized asteroid" unit for distance.
            # Position them on the side of the 'other_asteroid' where 'self' came from.
            offset_distance = other_asteroid.radius + new_radius + ASTEROID_MIN_RADIUS

            new_position = other_asteroid.position + direction_vector * offset_distance

            # New velocity: move away in that direction +/- 30 degrees
            angle_offset = random.uniform(-30, 30)
            new_velocity = direction_vector.rotate(angle_offset) * (self.velocity.length() * 1.2) # Faster

            new_asteroids.append(Asteroid(new_position.x, new_position.y, new_radius, new_velocity))

        return new_asteroids

    def randomize_velocity_slightly(self):
        # Randomly change velocity by a small amount (e.g., +/- 10-20 degrees and speed change)
        angle_change = random.uniform(-20, 20) # degrees
        speed_multiplier = random.uniform(0.8, 1.2) # 80% to 120% of current speed
        self.velocity = self.velocity.rotate(angle_change) * speed_multiplier
