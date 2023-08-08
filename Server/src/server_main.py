import socket
from _thread import *
import threading # 멀티쓰레딩
import threaded

client_sockets = []

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

print('>> Server Start with ip :', HOST)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))

server_socket.listen() # client의 접속 요청을 기다리도록 만듦
client,addr=server_socket.accept()
thr=threading.Thread(target=threaded,args=(client_sockets))
thr.Daemon=True
thr.start()


