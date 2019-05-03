import socketserver
import sys

class TCP(socketserver.BaseRequestHandler):
     def handle(self):
         print('client access: {0} '.format(self.client_address[0]))
         sock = self.request

         buffer=sock.recv(1024)
         received = str(buffer, encoding='utf-8')