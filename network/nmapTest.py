import nmap

# Create an instance of the `nmap.PortScanner` class
nm = nmap.PortScanner()

# Specify the target host or network and the ports to scan
target = "192.168.1.1"  # Replace with your target
ports = '1-1000'  # Specify the port range

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

if __name__ == "__main__":
    testScan()