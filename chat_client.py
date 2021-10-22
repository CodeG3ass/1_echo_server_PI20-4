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
    reply_msg = sock.recv(1024).decode('utf-8')
    print('сообщение сервера: ', reply_msg)
