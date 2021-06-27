from constants import *
import pygame, ball
from datetime import datetime


pygame.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

hours_group = pygame.sprite.Group()
minutes_group = pygame.sprite.Group()
seconds_group = pygame.sprite.Group()



hour, minute, second, tick_counter = 0, 0, 0, 0

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
        update()

    pygame.quit()




def draw():
    surface.fill((200, 200, 200))

    make_balls()
    hours_group.draw(surface)
    minutes_group.draw(surface)
    seconds_group.draw(surface)

    draw_clock()
    pygame.display.flip()


def update():
    hours_group.update()
    minutes_group.update()
    seconds_group.update()

def draw_clock():
    x,y = GAME_WIDTH // 2 , GAME_HEIGHT // 2
    message_display(get_time_formated(), x, y)


def get_time_formated():
    global hour, minute, second
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
    textSurface = font.render(str(text), True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def message_display(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf',FONT_SIZE)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    surface.blit(TextSurf, TextRect)

def make_balls():

    global hour, minute, second, tick_counter

    ticks = pygame.time.get_ticks()
    if ticks - tick_counter > 60:
        tick_counter = ticks
        hour = int(hour)
        minute = int(minute)
        second = int(second)

        lhg = len(hours_group)
        lmg = len(minutes_group)
        lsg = len(seconds_group)

        if hour == 12 and minute == 59 and second == 59:
            hours_group.empty()

        if minute == 0 :
            minutes_group.empty()

        if second == 0:
            seconds_group.empty()


        if hour > lhg:
            for h in range(hour - lhg):
                hours_group.add(ball.Ball(99 // 2, 3,  (255, 0, 0)))

        if minute > lmg:
            for h in range(minute - lmg):
                minutes_group.add(ball.Ball(66 // 2, 6,  (0, 255, 0)))

        if second > lsg:
            for h in range(second - lsg):
                seconds_group.add(ball.Ball(33 // 2, 9, (0, 0, 255)))

if __name__ == "__main__":
    main()
