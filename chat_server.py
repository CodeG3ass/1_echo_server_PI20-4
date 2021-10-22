import socket

nickname = ''
while nickname == '':
    nickname = input('Введите никнейм: ')
sock = socket.socket(type=socket.SOCK_DGRAM)
while True:
    data = input("Введите данные для отправки: ")
    if data == 'exit':
        print('Соединение разорвано')
        sock.close()
        break
    data = nickname + ': ' + data
    sock.sendto(data.encode(), ('localhost', 9090))
    data = sock.recvfrom(1024)
    print(f'Данные от сервера: {data[0].decode()}, {data[1]}')
sock.close()
