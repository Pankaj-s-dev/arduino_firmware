import socket
import threading

from numpy import array

con_port = 1234
# host_ip = '0.0.0.0'
host_ip = socket.gethostbyname(socket.gethostname())
s_addr = (host_ip, con_port)
decode_format = 'utf-8'
d_msg = "!DISCONNECT"
size = 64
get_conn = []
a = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(s_addr)

def handle_client(conn, c_addr):
    print(f"[NEW CONECTION] {c_addr} connected.")
    connection = True
    while connection:
        msg_length = conn.recv(size).decode(decode_format)
        if msg_length:
            msg_length = int(msg_length)
            c_msg = conn.recv(msg_length).decode(decode_format)
            if c_msg == d_msg:
                connection = False
                
            print(f"[{c_addr}] {c_msg}")
            
    conn.close()


def handle():
    server.listen()
    print(f"[LISTENING]: server is listening on {host_ip}")
    while True:
        conn, c_addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, c_addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]: {threading.activeCount()-1}")

print("[STARTING] server is started....")
handle()