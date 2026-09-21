network_data = {}
new_network = input("Please enter your new Ip network: ")
open_ports = []
open_ports.append(input("Please enter the fist open port: ")) 
open_ports.append(input("Please enter the second open port: ")) 
network_data[new_network] = open_ports
print("Network Database:", network_data)


