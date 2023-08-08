import pygame
import pyautogui
import sys
import socket
import threading


pygame.init()
pygame.display.set_caption('helloworld')
height=960
width=1200


enemy_img = pygame.image.load('dd.png')
imgw=enemy_img.get_size()[0]
imgh=enemy_img.get_size()[1]
enex=0
eney=imgw

def consoles():
    global eney,enex
    while True:
        msg=client.recv(1024)
        if(msg.decode()=='up'):
            eney-=30
        elif(msg.decode()=='down'):
            eney+=30
        elif(msg.decode()=='right'):
            enex+=30
        elif(msg.decode()=='left'):
            enex-=30


def acceptC():
    global client
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('172.30.1.45',8080))

    thr=threading.Thread(target=consoles,args=())
    thr.Daemon=True
    thr.start()



def GameMain():
    global eney,enex
    screen = pygame.display.set_mode((width,height))
    fps = pygame.time.Clock()

    img = pygame.image.load('dd.png')
    imgh=img.get_size()[1]
    imgw=img.get_size()[0]
    x=0
    y=imgw


    while True:
        screen.fill((255,255,255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pyautogui.keyUp('up')
                    y-=30
                    msg="up"
                    client.sendall(msg.encode())
                elif event.key == pygame.K_DOWN:
                    pyautogui.keyUp('down')
                    y+=30
                    msg="down"
                    client.sendall(msg.encode())
                elif event.key == pygame.K_RIGHT:
                    pyautogui.keyUp('right')
                    x+=30
                    msg="right"
                    client.sendall(msg.encode())
                elif event.key == pygame.K_LEFT:
                    pyautogui.keyUp('left')
                    x-=30
                    msg="left"
                    client.sendall(msg.encode())


        if img.get_size()[0]+x >= width:
            x=width-img.get_size()[0]
        elif x <= 0:
            x=0
        if img.get_size()[1]+y >= height:
            y=height-img.get_size()[1]
        elif y <= 0:
            y=0

        if enemy_img.get_size()[0]+enex >= width:
            enex=width-enemy_img.get_size()[0]
        elif enex <= 0:
            enex=0
        if enemy_img.get_size()[1]+eney >= height:
            eney=height-enemy_img.get_size()[1]
        elif eney <= 0:
            eney=0
            
            
        screen.blit(img,(x,y))
        screen.blit(enemy_img,(enex,eney))

        pygame.display.update()
        fps.tick(60)


if __name__ == '__main__':
    acceptC()
    GameMain()