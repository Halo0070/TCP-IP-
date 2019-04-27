import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect( ('192.168.35.138',8585) )
sock.send( "hello".encode() )
data= sock.recv( 65535 )   
print( "데이터를 돌려받았다 : ", data )