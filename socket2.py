import socketserver
import sys

class TCP(socketserver.BaseRequestHandler):
     def handle(self):
         print('client access: {0} '.format(self.client_address[0]))
         sock = self.request

         buffer=sock.recv(1024)
         received = str(buffer, encoding='utf-8')

         print('receive : {0}'.format(received))

        # 수신한 데이터를 그대로 돌려보냄.
         sock.send(buffer)  # 수신한 데이터를 그대로 클라이언트로 다시 송신.
         print('transmission : {0} '.format(received))
         sock.close()

if __name__ == '__main__':