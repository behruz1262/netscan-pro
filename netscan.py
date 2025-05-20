import socket
import ipaddress
import subprocess
import threading
import csv
import os
from tabulate import tabulate

# Get local IP and subnet (macOS-compatible)
local_ip = os.popen("ipconfig getifaddr en0").read().strip()
subnet = ipaddress.IPv4Network(local_ip + '/24', strict=False)

# Scan a single host
live_hosts = []
def ping(ip):
    try:
        output = subprocess.check_output(['ping', '-c', '1', '-W', '1', str(ip)], stderr=subprocess.DEVNULL)
        live_hosts.append(str(ip))
    except subprocess.CalledProcessError:
        pass

print("[*] Scanning for live hosts...")
threads = []
for ip in subnet.hosts():
    t = threading.Thread(target=ping, args=(ip,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()

print(f"\n[+] Live Hosts: {len(live_hosts)}")

# Scan ports on live hosts
def scan_ports(ip):
    ports = [22, 80, 443, 139, 445]
    open_ports = []
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    return open_ports

results = []
for host in live_hosts:
    ports = scan_ports(host)
    results.append([host, ', '.join(str(p) for p in ports)])

# Print results
print("\n[+] Scan Results:")
print(tabulate(results, headers=["IP Address", "Open Ports"]))

# Export results to CSV
with open("results.csv", "# Export results to CSV
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["IP Address", "Open Ports"])
    for row in results:
        writer.writerow(row)
print("\n[+] Results saved to results.csv")
", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["IP Address", "Open Ports"])
    for row in results:
        writer.writerow(row)
print("\n[+] Results saved to results.csv")
    


    
    
    
                                                                                
^G Get Help  ^O WriteOut  ^R Read File ^Y Prev Pg   ^K Cut Text  ^C Cur Pos   
^X Exit      ^J Justify   ^W Where is  ^V Next Pg   ^U UnCut Text^T To Spell  
