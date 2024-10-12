import nmap

# Create an instance of the `nmap.PortScanner` class
nm = nmap.PortScanner()

# Specify the target host or network and the ports to scan
target = "192.16.1.1"  # Replace with your target
ports = '1-200'  # Specify the port range

# Perform the scan
nm.scan(hosts=target, ports=ports)

def scanPorts():
    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
            lport = list(nm[host][proto].keys())
            lport.sort()
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

if __name__ == "__main__":
    scanPorts()