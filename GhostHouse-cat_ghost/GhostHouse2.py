import pygame
import time
import random
import pygame as pg
                                                                                               #BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM

def draw():
    pygame.init()
    white = [255, 255, 255]

    size = [900, 600]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Ghost game, meow")

    done =  False
    score = 0

    while done == False:

        screen.fill(white)

        rand_door = random.randint(1,7)
        door_surf = pygame.image.load('texture\door'+str(rand_door)+'.jpg')
        door_rect = door_surf.get_rect(bottomright=(900, 500))
        screen.blit(door_surf, door_rect)

        draw_text(screen, "Какую дверь ты откроешь? Пройдено дверей: " + str(score))

        pygame.display.update()
        ghost_door = random.randint(1,3)

        ev = False

        buttons = set()

        buttons.add(pygame.K_1)
        buttons.add(pygame.K_2)
        buttons.add(pygame.K_3)
        buttons.add(pygame.K_9)

        while ev == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ev= True
                    done = True

                elif event.type == pygame.KEYDOWN:
                    if event.key in buttons:
                        ev = True

                    if event.key == pygame.K_1 and ghost_door == 1 or \
                                            event.key == pygame.K_2 and ghost_door == 2 or \
                                            event.key == pygame.K_3 and ghost_door == 3:
                        screen.fill(white)
                        pg.mixer.music.load('boo.mp3')
                        pg.mixer.music.play()
                        draw_text(screen, "BOOO!, hehe")
                        ghost_surf = pygame.image.load('texture\ghost1.jpg')
                        ghost_rect = ghost_surf.get_rect(bottomright=(900, 600))
                        screen.blit(ghost_surf, ghost_rect)
                        pygame.display.update()
                        done = True
                        time.sleep(3)
                    else:
                        score += 1

    pygame.quit()
    


        #pygame.display.update()

def draw_text(screen, text):
    font = pygame.font.Font(None, 30)
    black = [0, 255, 120]
    text = font.render(text, True, black)
    screen.blit(text, [30, 50])


def main():
    draw()

if __name__ == '__main__':
    main()
