import socket

#a socket object is created for communication
# S = socket.socket(socket_family, socket_type, protocol=0)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# now connect to the web server on port 80
# - the normal http port
clientsocket.connect(("www.studytonight.com", 80))
clientsocket.listen(5)

# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# #bind the socket to a public host and a well-known port
# serversocket.bind((socket.gethostname(), 80))

# #become a server socket and listen for connections
# serversocket.listen(5)
