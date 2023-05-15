# Port Management Script

This Python script allows you to turn on or release ports on your system by starting or stopping the associated services. It helps you free up ports that are in use by other programs, making them available for your own use.

## Prerequisites

- Python 3.x
- Root privileges (required for starting/stopping services)

## Usage

1. Clone the repository or download the `port_management.py` file.

2. Open a terminal and navigate to the script directory.

3. Run the script with the following command:

   > sudo python3 port_management.py

4. Choose one of the options from the menu:

- **1. Turn on a port**: Enter the port number you want to activate. The script will start the associated service if it exists.

- **2. Release a port**: Enter the port number you want to release. The script will stop and disable the service using that port.

- **0. Exit**: Quit the script.

## Features

- Turn on a port by starting the associated service.
- Release a port by stopping and disabling the associated service.
- Automatic service discovery based on the port number.
- Interactive menu for user-friendly interaction.

## Notes

- This script requires root privileges to start and stop services. Please run it with `sudo`.

- It is important to ensure that the correct service names are associated with the respective ports in the script. Modify the script to update the service names as per your system configuration.

- If a port is already in use by another program, you will be prompted to release the port or choose a different one.

## License

This project is licensed under the [MIT License](LICENSE).
