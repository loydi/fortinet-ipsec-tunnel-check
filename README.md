# Fortinet IPSec Tunnel Check via SNMP

This repository contains scripts and tools for monitoring the status of IPSec VPN tunnels on Fortinet devices using SNMP. These tools can help network administrators ensure that VPN tunnels are up and running, and quickly identify any issues that may arise.

## Features

- Retrieve and display the status of IPSec Phase 1 and Phase 2 tunnels.
- Monitor VPN tunnel uptime and performance.
- Easily integrate with monitoring systems like Nagios.

## Requirements

- SNMP must be enabled on your Fortinet device.
- pip install easysnmp

## Getting Started

1. **Clone the Repository**

    ```sh
    git clone https://github.com/loydi/fortinet-ipsec-tunnel-check.git
    cd fortinet-ipsec-tunnel-check
    ```

2. **Configure SNMP on Fortinet Device**

    Ensure SNMP is enabled on your Fortinet device and the necessary MIB files are available.

3. **Install Dependencies**

    Ensure you have python and Net-SNMP installed on your system.

    ```sh
    sudo apt-get install snmp 
    ```

4. **Using the Scripts**

    Use the provided scripts to check the status of IPSec tunnels. For example:

    ```sh
    check_ipsec_tunnels.py -H <Fortigate_IP> -C <community_string>
    ```

    Replace `<Fortigate_IP>` with the IP address of your Fortinet device and `<community_string>` with your SNMP community string.
## Contributing
Contributions are welcome! If you'd like to contribute, please fork this repository, make your changes, and submit a pull request.

**Requesting New Features**

If you have an idea for a new feature or improvement, please open an issue to discuss it. We encourage the community to suggest enhancements and new functionalities.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
```css
This update includes a section in the Contributing part where users are encouraged to request new features, enhancing community involvement and continuous improvement of the project.
```
