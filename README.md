# Reverse Shell Nmap

This project demonstrates how to download, install, and use **Nmap** to create a **reverse shell** on a target machine.

**Important:** This tool is for educational purposes only and should only be used in authorized environments. Unauthorized use of this script is illegal and unethical.

---

## Requirements

- Python 3.x
- Nmap (for network scanning)
- Git

## Installation

To get started with this project, follow these steps:

### 1. Clone the Repository

Open a terminal or Bash shell and run the following command to clone the repository to your local machine:

```bash
git clone https://github.com/your-username/reverse-shell-nmap.git
```
### Navigate to the Project Directory
Once cloned, navigate into the project directory:
```bash
cd reverse-shell-nmap
```
### Download Nmap
If you don't already have Nmap installed, the script will automatically download it for you. You can manually download it by running:
```bash
python download_nmap.py
```
Run the Script
To execute the script, use the following command:
```bash
python reverse_shell.py
```
## Script Breakdown
Download Nmap: The script will download and install Nmap if not already present.

Reverse Shell: It establishes a reverse shell connection to a given IP and port.

Timeout: The script will keep the shell alive for 24 hours before it times out.

PowerShell Disable: Disables PowerShell real-time monitoring.

User Creation: Adds a new user (hacker) and gives it administrator privileges.

Port Logging: Logs active ports on the machine.
# Legal Notice
This script is intended for use in authorized environments, such as penetration testing on systems you own or have explicit permission to test.

By using this script, you agree to the following:

Educational Purpose Only: This tool is meant for learning and testing in a controlled environment.

No Unauthorized Use: You must not use this script to attack or infiltrate systems without explicit permission.

Legal Liability: You are responsible for ensuring the legality of your actions in your jurisdiction.

## License
This project is licensed under the MIT License - see the LICENSE file for details.





