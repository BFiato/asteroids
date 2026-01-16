import pygame
import random
from constants import *
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        return
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            
            #set up split parameters
            split_angle = random.uniform(20, 50)
            first_asteroid_angle = self.velocity.rotate(split_angle)
            second_asteroid_angle = self.velocity.rotate(-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            #create new asteroids
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = first_asteroid_angle * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = second_asteroid_angle * 1.2