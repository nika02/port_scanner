import socket

host = socket.gethostname()

for portNum in range(65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((host, portNum))

    if result == 0:
        print("Port {} is open".format(portNum))
        
    else:
        print("Port {} is closed".format(portNum))
        
    s.close()
