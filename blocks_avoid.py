import pygame
import random
from threading import Thread
pygame.init()
sc_w,sc_h=400,400
screen=pygame.display.set_mode((sc_w,sc_h))
clock=pygame.time.Clock()
change_delay=5
l_ch_tm=pygame.time.get_ticks()

running =True
cube_color=(240,250,210)
cube_size=20
cube_x=(sc_w-cube_size)//2
cube_y=(sc_h-cube_size)//2
cube_p=None
cube_ai=None
cube_speed=0.05
pose=sc_w-cube_size
def dr_cb(t=None,m=None):
    global cube_p
    if t==None or m==None:
        cube_p=pygame.draw.rect(screen,cube_color,(cube_x,cube_y,cube_size,cube_size))
    else:
        cube_p = pygame.draw.rect(screen, cube_color, (t, m, cube_size, cube_size))
cb_x=random.randint(0,sc_h-cube_size)
def dr_cb_wl(x,y,c):
    global cube_ai
    if c==1:
        cube_ai=pygame.draw.rect(screen,cube_color,(y,x,cube_size,cube_size))
    else:cube_ai=pygame.draw.rect(screen,cube_color,(x,y,cube_size,cube_size))
def game_over():
    screen.fill((0, 0, 0))
    fnt=pygame.font.Font(None,36)
    t_sur=fnt.render("Game Over",True,(255,10,10))
    px,py=(screen.get_width()-t_sur.get_width())/2,(screen.get_height()-t_sur.get_height())/2
    screen.blit(t_sur,(px,py))
_timer=True
dir_rd=0
while running:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            running=False
            break
    if i.type == pygame.KEYDOWN:
        if _timer:
            if i.key==pygame.K_LEFT:
                cube_x=max(cube_x-cube_speed,0)
            elif i.key==pygame.K_RIGHT:
                cube_x=min(cube_x+cube_speed,sc_w-cube_size)
            elif i.key==pygame.K_UP:
                cube_y=max(cube_y-cube_speed,0)
            elif i.key==pygame.K_DOWN:
                cube_y=min(cube_y+cube_speed,sc_h-cube_size)
        else:
            if i.key == pygame.K_RETURN:
                _timer = True
                cube_x = (sc_w - cube_size) // 2
                cube_y = (sc_h - cube_size) // 2
                dr_cb(cube_x,cube_y)


    c_time=pygame.time.get_ticks()
    if _timer:
        
        if c_time-l_ch_tm>=change_delay:
            #print("change detected")
            l_ch_tm=c_time
            pose-=1
            if pose==0:
                dir_rd=random.randint(0,1)
                pose=sc_w-cube_size
                cb_x=random.randint(0,sc_h-cube_size)

    screen.fill((0,0,0))
    dr_cb()
    dr_cb_wl(cb_x,pose,dir_rd)
    if cube_ai.colliderect(cube_p):
        #print("collision detected")
        _timer=False
        #running=False
        game_over()
    pygame.display.flip()
pygame.quit()