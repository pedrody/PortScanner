import socket

adress = input('Adress -> ')
e = input('[1] - Use a port list\n'
	  '[2] - Add manual port\n'
	  '-> ')

port_list = [21, 22, 80, 443, 445, 3306, 25]
add_manual = []

if int(e) == 1:
	for port in port_list:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(0.1)
		code = client.connect_ex((adress,  port))
		if code == 0:
			print(port, "< OPEN >")
		else:
			print(port, '< CLOSED >')
if int(e) == 2:
	i = 0
	am_port = int(input('How many ports? '))
	while i < am_port:
		ports = int(input('Port -> '))
		add_manual.append(ports)
		i += 1
	for port in add_manual:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(0.1)
		code = client.connect_ex((adress,  port))
		if code == 0:
			print(port, "< OPEN >")
		else:
			print(port, '< CLOSED >')
			
