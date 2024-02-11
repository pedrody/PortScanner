import socket
import argparse

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


def main():
    parser = argparse.ArgumentParser(
        description='Scan open ports on a given address.'
    )
    parser.add_argument(
        'address',
        type=str,
        help='The IP address to scan.'
    )

    parser.add_argument(
        '-p', '--ports',
        nargs='+',
        type=int,
        help='List of ports to scan'
    )

    parser.add_argument(
        '-t', '--timeout',
        type=float,
        default=0.5,
        help='Timeout for port connection (default: 0.5)'
    )

    parser.add_argument(
        '-sF', '--save-file',
        type=str,
        help='Path to save the file with the output information'
    )

    args = parser.parse_args()

    if not args.ports:
        args.ports = [21, 22, 25, 80, 443, 445, 3306]
    
    open_ports = get_open_ports(args.address, args.ports, args.timeout)

    output = []
    for port in args.ports:
        status = 'OPEN' if port in open_ports else 'CLOSED'
        output.append(f'{port} {status}')
        print(f'{port} {status}') 

if __name__ == '__main__':
    main()
