import socket, sys

HOST = '127.0.0.1'
PORT = 8001
BUFFER_SIZE = 1024

def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

def main():
    remoteHost = 'www.google.com'
    remotePort = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxyStart:
        print("Starting...")

        # allow reused addresses, bind, and set to listening mode
        proxyStart.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxyStart.bind((HOST, PORT))
        proxyStart.listen(1)

        while True:
            connStart, addrStart = proxyStart.accept()
            print("Connected by:", addrStart)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxyEnd:
                print("Connecting to Google")
                remoteIp = get_remote_ip(remoteHost)

                # connect to google
                proxyEnd.connect((remoteIp, remotePort))

                # getting data from proxyStart's connection
                sendData = connStart.recv(BUFFER_SIZE)
                print("Sending data to google")
                proxyEnd.sendall(sendData)

                proxyEnd.shutdown(socket.SHUT_WR) #shutdown the proxy

                receivedData = proxyEnd.recv(BUFFER_SIZE)

                print("Sending data back to client")
                connStart.send(receivedData)

            connStart.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()