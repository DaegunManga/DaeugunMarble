import socket
from _thread import *

client_sockets = []

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

print('>> Server Start with ip :', HOST)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))



server_socket.listen() # client의 접속 요청을 기다리도록 만듦

"""client의 접속 요청이 들어왔을 때 실행되는 함수"""
def threaded(client_socket, addr):
    print('>> Connected by :', addr[0], ':', addr[1])

    ## 끊길 때까지 반복
    while True:
        try:
            ## 데이터를 받으면, 저장
            data = client_socket.recv(1024)

            if not data:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break

            print('>> Received from ' + addr[0], ':', addr[1], data.decode())

            ## chat to client connecting client ##
            ## chat to client connecting client except person sending message ##
            for client in client_sockets:
                if client != client_socket:
                    client.send(data)
        
        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break
    
    if client_socket in client_sockets:
        client_sockets.remove(client_socket)
        print('remove client list : ', len(client_sockets))

    client_socket.close()

try: # client의 접속 요청이 들어옴
    while True:
        print('>> Wait')

        client_socket, addr = server_socket.accept()
        client_sockets.append(client_socket)
        start_new_thread(threaded, (client_socket, addr))
        print("참가자 수 : ", len(client_sockets))
except Exception as e:
    print('에러 : ', e)

finally:
    server_socket.close()