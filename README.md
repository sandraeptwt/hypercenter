# HyperCenter

HyperCenter is a Python-based utility designed to enhance the Windows startup process by managing the programs that launch at boot. By enabling or disabling startup programs, users can significantly improve their system's boot time.

## Features

- **List Startup Programs**: Display all programs that are set to run at startup.
- **Disable Startup Programs**: Prevent specified programs from launching at boot.
- **Enable Startup Programs**: Allow specified programs to launch at boot.
- **Optimize Startup**: Provides an interface to easily disable unnecessary startup programs.

## Requirements

- Windows operating system
- Python 3.x

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/HyperCenter.git
    ```

2. Navigate to the project directory:
    ```bash
    cd HyperCenter
    ```

3. Run the program:
    ```bash
    python hypercenter.py
    ```

## Usage

1. Run the program using the command above.
2. The program will list all the startup programs.
3. Enter the names of the programs you wish to disable (separated by commas) when prompted.

## Note

- **Administrator Rights**: Some features may require administrative privileges to modify registry keys.
- **Backup**: It is recommended to backup your registry before making changes.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.