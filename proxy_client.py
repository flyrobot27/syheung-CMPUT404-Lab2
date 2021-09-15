import socket

HOST = 'localhost'
PORT = 8001
BUFFER_SIZE = 1024

PAYLOAD = "Get / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

def connect(addr):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addr)
        s.sendall(PAYLOAD.encode())
        s.shutdown(socket.SHUT_WR)

        data = s.recv(BUFFER_SIZE)
        print(data)
    except Exception as e:
        print(e)
    
    finally:
        s.close()

if __name__ == '__main__':
    try:
        connect((HOST, PORT))
    except KeyboardInterrupt:
        exit()