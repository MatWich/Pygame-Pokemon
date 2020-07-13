import config
import pygame

class Npc:
    def __init__(self, x, y, textMessage, wantsToFight):
        self.position = [x, y]
        self.img = pygame.transform.scale(config.NPC1_IMG, (config.SCALE, config.SCALE))
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)
        self.textMessage = textMessage
        self.wantsToFight = wantsToFight

    def render(self, screen):
        self.rect = self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)
        screen.blit(self.img, self.rect)



    #Player potrzebny jak juz bedzie system walki
    def interact(self, screen, Player):
        Text = config.dialogFont.render(self.textMessage, 1, (config.BLACK))
        screen.blit(Text, (config.WIDTH/2 - Text.get_width(), config.HEIGHT - 100))
