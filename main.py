import socket
import argparse
from datetime import datetime

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
        'addresses',
        nargs='*',
        type=str,
        default=[],
        help='The IP address(es) to scan.'
    )

    parser.add_argument(
        '-aF', '--addresses-file',
        type=str,
        help='Path to file with addresses to scan, separeted by commas or spaces.'
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
    
    if args.addresses_file:
        with open(args.addresses_file, 'r') as file:
            args.addresses = [
                address.strip() for line in file \
                for address in line.strip().split(',')
            ]
    
    for address in args.addresses:
        output = []
        open_ports = get_open_ports(address, args.ports, args.timeout)
        info_msg = (
            f'\nScan Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n'
            f'Target: {address}\n'
        )
        output.append(info_msg)
        print(info_msg)

        for port in args.ports:
            status = 'OPEN' if port in open_ports else 'CLOSED'
            output.append(f'{port} {status}')
            print(f'{port} {status}') 

        if args.save_file:
            output_file = f'{args.save_file}.txt'
            with open(output_file, 'a') as file:
                for line in output:
                    file.write(f'{line}\n')
        
            print(f'\nOutput saved to "{output_file}"\n')

if __name__ == '__main__':
    main()
