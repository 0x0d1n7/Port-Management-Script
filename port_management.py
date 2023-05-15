import subprocess
import os
import sys

def check_root_privileges():
    if os.geteuid() != 0:
        print("This script requires root privileges. Please run the script with 'sudo'.")
        sys.exit(1)

def get_service_name(port):
    try:
        # Execute lsof command to get the service name using the port
        result = subprocess.run(["sudo", "lsof", "-i", f"TCP:{port}"], capture_output=True, text=True)
        output = result.stdout

        if output:
            # Extract the service name from the output
            lines = output.strip().split('\n')
            service_name = lines[1].split()[0]
            return service_name

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def turn_on_port(port):
    try:
        # Enable the service associated with the port
        service_name = get_service_name(port)

        if service_name:
            subprocess.run(["sudo", "systemctl", "start", service_name])
            print(f"The service associated with port {port} ({service_name}) has been started.")
        else:
            print(f"No service found using port {port}.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def release_port(port):
    try:
        # Check if port is in use
        service_name = get_service_name(port)

        if service_name:
            subprocess.run(["sudo", "systemctl", "stop", service_name])
            subprocess.run(["sudo", "systemctl", "disable", service_name])
            print(f"The service using port {port} ({service_name}) has been stopped and disabled.")
        else:
            print(f"No service found using port {port}.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def show_menu():
    print("Select an option:")
    print("1. Turn on a port")
    print("2. Release a port")
    print("0. Exit")

def get_menu_choice():
    choice = input("Enter your choice: ")
    return choice

# Check if script is run with root privileges
check_root_privileges()

while True:
    show_menu()
    choice = get_menu_choice()

    if choice == '1':
        port = input("Enter the port number to turn on: ")
        turn_on_port(port)

    elif choice == '2':
        port = input("Enter the port number to release: ")
        release_port(port)

    elif choice == '0':
        print("Exiting the script.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
