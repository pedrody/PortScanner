# PortScanner
This is a simple Python script that checks whether the ports on an IP address are open or closed.

## How it works
The script uses Python's socket library to create TCP connections on the specified ports and check whether they are open or closed. The script accepts two port scanning options: a predefined list of ports and a custom list of ports provided by the user.

## How to use
- To use the script, follow the steps below:
1. Clone this repository to your local machine.
2. Open the terminal or command prompt and navigate to the directory where the repository was cloned.
3. Run the script by typing python port_scan.py.
4. Enter the IP address you want to check.
5. Select one of the port scanning options:
Use a predefined list of ports.
Manually add the ports you want to check.  

- If you chose the predefined port list option, the script will check whether the ports listed below are open or closed:  
21 (FTP)  
22 (SSH)  
80 (HTTP)  
443 (HTTPS)  
445 (SMB)  
3306 (MySQL)  
25 (SMTP)  

- If you chose the option to manually add ports, enter the number of ports you want to check and type in the port numbers **separated by a space**.
The script will display a list of open ports and a list of closed ports on the provided IP address.

## Requirements
To run the script, you will need Python 3 installed on your machine. Additionally, the script uses only standard Python libraries, so there is no need to install any additional libraries.

## Disclaimer
This script is for educational purposes only and should not be used to perform port scans on computers or networks without permission. Improper use of the script may result in security breaches and may be illegal in your jurisdiction.
