import socket			

s = socket.socket()		
host = socket.gethostname()	        # Get current machine name
print("host name: ", host)
port = 9999			                # Client wants to connect to server's
print("port is: ", port)
				                    # port number 9999
s.connect((host,port))
print(s.recv(1024))		            # 1024 is bufsize or max amount 
				                    # of data to be received at once
s.close()