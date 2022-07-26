import socket
import threading

con_port = 1234
host_ip = socket.gethostbyname(socket.gethostname())
s_addr = (host_ip, con_port)
decode_format = 'utf-8'
d_msg = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
client.connect(s_addr)