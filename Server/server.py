import pygame as pg #게임을위한 메인모듈
import pyautogui #조작감살짝 늘리기
import sys #콘솔창제어
import socket #소켓
import threading #멀티쓰레딩


pg.init() #시작
pg.display.set_caption('server') #제목
WindowSize = (960, 1200)
height=WindowSize[1] #세로
width=WindowSize[0] #가로

background_img = pg.image.load('./Image/background.png', ) # 배경
background_img = pg.transform.scale(background_img, WindowSize)

enemy_img = pg.image.load('dd.png') #이미지로드
imgw=enemy_img.get_size()[0] #[0]은 이미지 가로길이
imgh=enemy_img.get_size()[1] #[1]은 이미지 세로길이
enex=0 #현재 적의 x좌표
eney=imgw #현재 적의 y좌표

def consoles():
    global eney,enex

    try:
        while True:
            print('>> Wait')

            client_socket, addr = server.accept()
            client_sockets.append(client_socket)
            start_new_thread(threaded, (client_socket, addr))
            print("참가자 수 : ", len(client_sockets))
    except Exception as e:
        print('에러 : ', e)

    finally:
        server_socket.close()

    while True:
        msg=client.recv(1024)
        print(msg)
        if(msg.decode()=='up'): #소켓으로부터받은데이터가 up일경우 적y좌표조정
            eney-=30
        elif(msg.decode()=='down'): #소켓으로부터받은데이터가 down일경우 적y좌표조정
            eney+=30
        elif(msg.decode()=='right'): #소켓으로부터받은데이터가 right일경우 적x좌표조정
            enex+=30
        elif(msg.decode()=='left'): #소켓으로부터받은데이터가 left일경우 적x좌표조정
            enex-=30


def acceptC():
    global client,server,addr
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('172.30.1.45',8080))
    server.listen(4)
    client,addr=server.accept()

    thr=threading.Thread(target=consoles,args=())
    #클라이언트로부터 받는 데이터를 관리하기위한
    #멀티쓰레딩(밑에는 데몬스레드라고 선언 -> c++로 따지면 detach와같습니다)
    thr.Daemon=True
    thr.start()



def GameMain():
    global eney,enex
    screen = pg.display.set_mode((width,height))
    fps = pg.time.Clock()

    img = pg.image.load('dd.png') #이미지불러오기
    imgh=img.get_size()[1]
    imgw=img.get_size()[0]
    x=0
    y=imgw


    while True:
        #screen.blit(background_img, (0, 0))
        screen.fill((255,255,255))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    pyautogui.keyUp('up')
                    #이걸하는이유는 키보드를 꾹누르고있으면 원래는 한번가는데
                    #이걸하면은 쭉누르면 쭉갑니다
                    y-=30
                    msg="up"
                    client.sendall(msg.encode()) #클라이언트에게 내가내린명령전송
                elif event.key == pg.K_DOWN:
                    pyautogui.keyUp('down')
                    y+=30
                    msg="down"
                    client.sendall(msg.encode())
                elif event.key == pg.K_RIGHT:
                    pyautogui.keyUp('right')
                    x+=30
                    msg="right"
                    client.sendall(msg.encode())
                elif event.key == pg.K_LEFT:
                    pyautogui.keyUp('left')
                    x-=30
                    msg="left"
                    client.sendall(msg.encode())


        if img.get_size()[0]+x >= width: #x좌표조절
            x=width-img.get_size()[0]
        elif x <= 0:
            x=0
        if img.get_size()[1]+y >= height: #y좌표조절(스크린에서 안나가게끔)
            y=height-img.get_size()[1]
        elif y <= 0:
            y=0

        if enemy_img.get_size()[0]+enex >= width: #위와같습니다
            enex=width-enemy_img.get_size()[0]
        elif enex <= 0:
            enex=0
        if enemy_img.get_size()[1]+eney >= height:
            eney=height-enemy_img.get_size()[1]
        elif eney <= 0:
            eney=0
            
        screen.blit(img,(x,y)) #이미지그리기
        screen.blit(enemy_img,(enex,eney)) #이미지그리기

        pg.display.update() #디스플레이 업데이트
        fps.tick(60) #fps는 60


if __name__ == '__main__':
    acceptC() 
    GameMain()