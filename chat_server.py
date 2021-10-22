import socket

sock = socket.socket(type=socket.SOCK_DGRAM)
sock.bind(('localhost', 9090))
while True:
    data, addr = sock.recvfrom(1024)
    print(f'{addr}:', data.decode())
    reply_msg = input('Ответить: ')
    sock.sendto(reply_msg.encode(), addr)
sock.close()