import socket

ADDRESS = input('Address -> ')
USE_PORT_LIST = 1
ADD_MANUAL = 2
TIMEOUT = 0.1

def get_open_ports(address, ports, timeout):
    open_ports = []
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(timeout)
        code = client.connect_ex((address,  port))
        if code == 0:
            open_ports.append(port)
        client.close()
    return open_ports

option = int(input('[1] - Use a port list\n'
                   '[2] - Add manual port\n'
                   '-> '))

if option == USE_PORT_LIST:
    port_list = [21, 22, 80, 443, 445, 3306, 25]
    open_ports = get_open_ports(ADDRESS, port_list, TIMEOUT)
    for port in open_ports:
        print(f"{port} < OPEN >")
    for port in port_list:
        if port not in open_ports:
            print(f"{port} < CLOSED >")

elif option == ADD_MANUAL:
    num_ports = int(input('How many ports? '))
    add_manual = [int(port.strip()) for port in input('Ports (separated by spaces or commas) -> ').split()]
    open_ports = get_open_ports(ADDRESS, add_manual, TIMEOUT)
    for port in open_ports:
        print(f"{port} < OPEN >")
    for port in add_manual:
        if port not in open_ports:
            print(f"{port} < CLOSED >")
else:
    print('Invalid option')
