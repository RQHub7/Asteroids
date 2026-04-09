import pygame

class ScoreBoard(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # We must call the parent constructor to work with Groups
        super().__init__(self.containers)
        self.score = 0
        self.font = pygame.font.Font(None, 24)
        self.x = x
        self.y = y
        self.re_render()

    def re_render(self):
        # This creates the image only when called
        self.image = self.font.render(f"Score: {self.score}", True, (57, 255, 20))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update_score(self, points):
        self.score += points
        self.re_render()

    def update(self, dt):
        # The ScoreBoard doesn't need to move every frame
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)