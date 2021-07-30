import socket

# Server
def clntconn(host, port, key):
    
    # Create socket object, omits Close()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
         
        # Connect using IPV4 AF
        sock.connect((host,port))
        
        # Encode string send bytes
        sock.sendall(str(key).encode('utf-8')) 

        # Send data to socket
        data = sock.recv(1024)

    # Decode message and print
    print('Received: ', repr(data.decode()))

# Create connection
clntconn('127.0.0.1', 65432,'This!Password¿IsSecure_♣')