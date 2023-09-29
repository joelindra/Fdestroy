# FTP Login Destroyer

**Overview:** FTP Login Destroyer is a versatile Python script designed to assess the security of FTP (File Transfer Protocol) servers by testing login credentials. It provides a flexible and user-friendly approach to identify potential vulnerabilities in FTP server configurations.

## Features

- **Multiple Target Sources:** The script allows users to choose between two methods for specifying target hosts:
  - Input a list of target hosts from a file, with one host per line.
  - Input a single target host interactively.
  
- **Port Accessibility Check:** Before attempting login, the script checks if port 21 (the default FTP port) is open on the target host. This initial check helps to avoid unnecessary login attempts.

- **Anonymous Login:** The script attempts to log in to the FTP server using the default "anonymous" username and "anonymous" password. This allows it to test for common anonymous login misconfigurations.

## Usage

1. Clone the repository or download the script.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the script and choose your target input method:
   - Option 1: Input a list of target hosts from a file.
   - Option 2: Input a single target host interactively.
4. The script will initiate the testing process, providing visual feedback during the login attempts.
5. Successfully logged-in hosts are recorded in the "vuln.txt" file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions to this project are welcome. Please feel free to submit issues, feature requests, or pull requests.

## Disclaimer

FTP Login Destroyer is a tool designed for ethical and responsible use, such as testing your own FTP servers or those with explicit permission for assessment. Unauthorized use of this script to access FTP servers without proper authorization is strictly prohibited and may violate legal and ethical guidelines.

&copy; 2023 FTP Login Destroyer Joelindra. All rights reserved.
