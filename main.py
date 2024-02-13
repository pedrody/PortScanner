import socket
import argparse
from datetime import datetime

# ANSI colors
RESET_CLR = '\033[0m'
BOLD = '\033[1m'
RED_CLR = '\033[91m'
GREEN_CLR = '\033[92m'

def get_open_ports(address, ports, timeout):
    """
    The function `get_open_ports` takes an address, a list of ports, and a timeout
    value as input, and returns a list of open ports on that address.
    
    :param address: The address parameter is the IP address or hostname of the
    target device or server that you want to scan for open ports
    :param ports: The "ports" parameter is a list of port numbers that you want to
    check for open ports on the specified address
    :param timeout: The timeout parameter is the maximum amount of time (in seconds)
    that the socket will wait for a connection attempt to succeed before timing out
    :return: a list of open ports.
    """

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
    # Setting up the parser to process command-line arguments
    parser = argparse.ArgumentParser(
        description='Scan open ports on a given address.'
    )

    # Argument to specify the IP addresses to be scanned
    parser.add_argument(
        'addresses',
        nargs='*',
        type=str,
        default=[],
        help='The IP address(es) to scan.'
    )

    # Argument to specify a file containing IP addresses to be scanned
    parser.add_argument(
        '-aF', '--addresses-file',
        type=str,
        help='Path to file with addresses to scan, separeted by commas or spaces.'
    )

    # Argument to specify the ports to be scanned
    parser.add_argument(
        '-p', '--ports',
        nargs='+',
        type=int,
        help='List of ports to scan'
    )

    # Argument to specify the timeout for port connection
    parser.add_argument(
        '-t', '--timeout',
        type=float,
        default=0.5,
        help='Timeout for port connection (default: 0.5)'
    )

    # Argument to specify a file to save the results
    parser.add_argument(
        '-sF', '--save-file',
        type=str,
        help='Path to save the file with the output information'
    )

    # Parsing command-line arguments
    args = parser.parse_args()

    # If the user does not specify ports, standard common ports will be used
    if not args.ports:
        args.ports = [21, 22, 25, 80, 443, 445, 3306]
    
    # If the user specifies an addresses file, read addresses from the file and
    # save in "args.addresses"
    if args.addresses_file:
        with open(args.addresses_file, 'r') as file:
            args.addresses = [
                address.strip() for line in file \
                for address in line.strip().split(',')
            ]
    
    # For each specified address, perform port scanning
    for address in args.addresses:
        output = []
        open_ports = get_open_ports(address, args.ports, args.timeout)
        # Creating an information message about scanning
        info_msg = (
            f'\nScan Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n'
            f'Target: {address}\n'
        )
        output.append(info_msg)
        # Printing the informative message to the terminal
        print(f'{BOLD}{info_msg}{RESET_CLR}')

        # For each specified port, check if it's open or closed
        for port in args.ports:
            status = 'OPEN' if port in open_ports else 'CLOSED'
            status_clr = GREEN_CLR if port in open_ports else RED_CLR
            output.append(f'{port} {status}')
            # Printing the port status to the terminal
            print(f'{status_clr}{port} {status}{RESET_CLR}') 

        # If specified, save the results to a file
        if args.save_file:
            output_file = f'{args.save_file}.txt'
            with open(output_file, 'a') as file:
                for line in output:
                    file.write(f'{line}\n')
            # Printing a message informing that the results have been saved
            print(f'\nOutput saved to "{output_file}"\n')

if __name__ == '__main__':
    main()
