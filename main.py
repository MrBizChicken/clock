from constants import *
import pygame
from datetime import datetime


pygame.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

hour = 0

pygame.init()

def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()

        draw()

    pygame.quit()


def draw():
    print(hour)
    surface.fill((200, 200, 200))
    draw_clock()
    pygame.display.flip()


def draw_clock():
    x,y = GAME_WIDTH // 2 , FONT_SIZE
    message_display(get_time_formated(), x, y)


def get_time_formated():
    global hour
    # year, month, day, hour, minute, second
    #now = datetime(2020, 5, 17, 0,0,0)   #may 5th 2020 12:00:00
    now = datetime.now()

    hour = int(now.strftime("%H"))
    if hour > 12:
        hour = hour - 12

    if hour == 0:
        hour = 12

    minute = str(now.strftime("%M"))
    second = str(now.strftime("%S"))

    t = str(hour)
    t += ":"
    t += minute
    t += ":"
    t +=  second
    return t


def text_objects(text, font):
    textSurface = font.render(str(text), True, (255, 255, 255))
    return textSurface, textSurface.get_rect()


def message_display(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf',FONT_SIZE)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    surface.blit(TextSurf, TextRect)


if __name__ == "__main__":
    main()
