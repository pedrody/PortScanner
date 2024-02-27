# Port Scanner

## 📖 Description
This project is a Python script for scanning open ports on specified IP addresses. It allows you to scan for open ports on individual addresses or multiple addresses provided in a file. The script utilizes the socket module to establish connections to target devices or servers and determine the status of specified ports.

The script establishes TCP connections to the specified IP addresses and ports. It checks whether the connections are successful to determine if the ports are open or closed. Results are displayed in the terminal and optionally saved to a text file.

## 🛠️ Features
- Scan Addresses: Allows scanning of open ports on IP addresses.
- Batch Scan: Supports scanning multiple IP addresses listed in a file.
- Custom Port Specification: Users can specify the ports to be scanned.
- Timeout Configuration: Allows configuring the timeout for port connection attempts.
- Save Results Option: Provides the option to save scan results to a text file.

## 📡 Technologies Used
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=for-the-badge)

## 💻 Usage
First, ensure you have Python and Git installed on your system.

You can clone this repository to your local machine using Git:
```
git clone https://github.com/pedrody/PortScanner.git
```
Navigate to the cloned repository:
```
cd PortScanner
```
Now you're ready to use the script!

You can execute it from your terminal, providing the following arguments:
```
python main.py [addresses] [-p PORTS] [-t TIMEOUT] [-sF SAVE_FILE]
```

### Command-line arguments
- `[addresses]`: Specify IP addresses (separated by spaces) to scan.
- `-aF, --addresses-file`: Specify a file with addresses to scan, separated by commas or spaces.
- `-p, --ports`: Specify the ports to scan (default ports: 21, 22, 25, 80, 443, 445, 3306).
- `-t, --timeout`: Set the timeout for port connection attempts (default: 0.5 seconds).
- `-sF, --save-file`: Specify where you want to save the scan results.

### Example Usage
Scan individuals addresses:
```
python main.py 192.168.0.1 192.168.0.33 www.google.com -p 80 443 -t 2
```

Scan addresses from a file:
```
python main.py -aF addresses.txt -p 22 80 443 -sF scan_results
```

## 🤝 Contributing
Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or create a pull request.

