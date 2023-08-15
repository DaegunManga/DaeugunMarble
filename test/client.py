import socket
from _thread import *
import sys

ID = input('참가할 ID를 입력해주세요 : ')


HOST = '172.30.1.45'
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_socket.send(ID.encode())

data = client_socket.recv(1024)
if data == 'FullServer : ' + ID :
    print('서버에 인원이 가득 찼습니다.')
    sys.exit()

def recv_data(client_socket):
    print('oK')
    while True:
        data = client_socket.recv(1024)
        print(">> Chatting received")
        print("ID : ", repr(data.decode()))
        

start_new_thread(recv_data, (client_socket,))
print('>> Connect Server')
print('Your Id : ' + ID)

print(ID)

while True:
    message = input('Send : ') + ID
    if message == 'quit':
        close_data = message
        break

    client_socket.send(message.encode())

client_socket.close()