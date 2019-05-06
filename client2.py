import socket
import sys

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('{0} <Bind IP> <Server IP> <Message>'.format(sys.argv[0]))
        sys.exit()

    bindIP = sys.argv[1]
    serverIP = sys.argv[2]
    message = sys.argv[3]

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM은 TCP socket을 뜻함.
    sock.bind((bindIP, 0))

    try:
        sock.connect((serverIP, 5425))  # 서버에 연결 요청