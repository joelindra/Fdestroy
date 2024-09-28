![image](https://github.com/user-attachments/assets/8f6c3b2c-0e71-4f22-8fe5-ae052617e21a)

## **FTP Login Destroyer**
The FTP Login Tester is a Python-based tool designed for testing anonymous FTP login access on a list of target hosts or a single target. It checks if the FTP port (port 21) is open and attempts to log in using default anonymous credentials. This tool is particularly useful for scanning multiple hosts in parallel using multithreading for efficient testing.

## **Key features include:**

- Multithreading: Handles multiple targets simultaneously to speed up testing.
- Flexible Input: Supports reading targets from a file or manually entering a single target.
- Real-time Progress Indicator: Displays a live progress animation while testing targets.
- Detailed Logging: Logs successful logins to vuln.txt and error messages to error.log for debugging and analysis.
- Color-coded Terminal Output: Uses colorama to highlight different messages for better clarity.
- This tool is ideal for penetration testers or system administrators performing security checks on FTP servers across a network.

A multithreaded Python tool to test FTP login access on a list of target hosts. The tool attempts to log in to the FTP server with anonymous credentials and logs any successful attempts. It also checks if the target's FTP port (port 21) is open before attempting to connect.
