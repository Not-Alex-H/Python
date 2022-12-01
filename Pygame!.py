### Pygame? ###
import pygame
win = pygame.display.set_mode((1360, 700))
pygame.display.set_caption("Pygame!")
xpos = 200
ypos = 200
wid = 50
hei = 50
vel = 10
run = True
def boundaries(x, y, w, h, v):
    if x + (w / 2) > 1300:
        x += -v
    if x + -(w / 2) < 0:
        x += v
    if y + (h / 2) > 700:
        y += -v
    if y + -(h / 2) < 0:
        y += -v
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        xpos += -vel
    if keys[pygame.K_d]:
        xpos += vel
    if keys[pygame.K_w]:
        ypos += -vel
    if keys[pygame.K_s]:
        ypos += vel
    win.fill((0, 0, 0))
    boundaries(xpos, ypos, wid, hei, vel)
    pygame.draw.rect(win, (255, 0, 255), (xpos, ypos, wid, hei))
    pygame.display.update()
    
pygame.quit()