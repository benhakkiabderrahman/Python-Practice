#--------------------------------Function---------------------------------

def analyze_port(port): 
    if port == 22 :
        return "ssh"
    elif port == 80 :
        return "HTTP"
    elif port == 443 :
        return "HTTPS"
    else:
        return "Unknown Service"

#--------------------------------List---------------------------------

target_ports = [22, 80, 8080, 443]

#--------------------------------loop---------------------------------

for port in target_ports :
    The_actual_port = analyze_port(port)
    print(f"Port {port} is {The_actual_port} ")