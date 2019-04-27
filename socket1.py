import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind( ('192.168.35.138', 8585) )
server_socket.listen(0)
client_socket , addr = server_socket.accept() 
data = client_socket.recv( 65535 )
client.socket.send( data )                          
print ( "Recieved Data : " , data.decode() )