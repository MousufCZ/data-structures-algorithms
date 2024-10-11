import nmap

# Create an instance of the `nmap.PortScanner` class
nm = nmap.PortScanner()

# Specify the target host or network and the ports to scan
target = "192.168.1.1"  # Replace with your target
ports = "1"  # Specify the port range

# Perform the scan
nm.scan(hosts=target, ports=ports)

def testScan():
    # Print the scan results
    print("Scanner info: ", nm.scaninfo())
    print("Command line: ", nm.command_line())
    print("All hosts: ", nm.all_hosts())
    print("Hostname: ", nm[target].hostname())
    print("State: ", nm[target].state())
    print("All protocols: ", nm[target].all_protocols())
    print("Keys: ", nm[target]['tcp'].keys())
    print("Has TCP port: ", nm[target].has_tcp(1))
    print("Scanner target information: \n", nm[target])

# https://pypi.org/project/python-nmap/
# https://nmap.org/book/man.html
# https://www.studytonight.com/network-programming-in-python/integrating-port-scanner-with-nmap
def scanPorts():
    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
            lport = nm[host][proto].keys()
            lport.sort()
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
#
#
#
if __name__ == "__main__":
    scanPorts()