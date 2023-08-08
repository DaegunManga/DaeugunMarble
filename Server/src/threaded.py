"""
client의 접속 요청이 들어왔을 때 실행되는 함수
메세지를 받으면, Game_main으로 값을 보내 각종 명령을 실행함.
"""

import Game_main

def threaded(client_socket, addr, client_sockets):
    print('>> Connected by :', addr[0], ':', addr[1])

    ## 끊길 때까지 반복
    while True:
        try:
            msg=client_socket.recv(1024)
            print(msg)
            if(msg.decode()=='up'): #소켓으로부터받은데이터가 up일경우 적y좌표조정
                eney-=30
            elif(msg.decode()=='down'): #소켓으로부터받은데이터가 down일경우 적y좌표조정
                eney+=30
            elif(msg.decode()=='right'): #소켓으로부터받은데이터가 right일경우 적x좌표조정
                enex+=30
            elif(msg.decode()=='left'): #소켓으로부터받은데이터가 left일경우 적x좌표조정
                enex-=30

        
        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break
    
    if client_socket in client_sockets:
        client_sockets.remove(client_socket)
        print('remove client list : ', len(client_sockets))

    client_socket.close()