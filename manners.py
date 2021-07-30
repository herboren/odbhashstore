import socket, authproc, pickle

# Server
def servconn(host, ports):
    
    # Create socket object, omits Close()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
         
        # A pair (host, port) is used
        # for the AF_INET address family
        sock.bind((host,ports))
        
        # Open Port
        sock.listen() 

        # Blocks and waits for incomming connection.
        conn, addr = sock.accept()        
        
        # Print successful connection
        print('Connection Established: ', addr)        

        while True:
            # 1024 bytes buffer
            data = conn.recv(1024)
                        
            # If data not present close connection
            if not data:
                break
            else:
                ukey = pickle.loads(data.decode('utf-8').strip())
                print(f'{ukey[0]}:{ukey[1]}')
                
                #authproc.accesscomm_record(authproc.establish_accesscomm(),'username123',authproc.hash_key(authproc.zest_key(), 'This!Password¿IsSecure_♣'))
                # Send data to socket
                conn.sendall(data)

# Start Server
servconn('127.0.0.1', 65432)