from ftplib import FTP
import socket
import time
import threading
import logging
from colorama import Fore, Style, init

# Initialize colorama
init()

# Lock for thread-safe file access
file_lock = threading.Lock()

# Initialize logger
logging.basicConfig(filename='error.log', level=logging.ERROR)

def is_port_open(hostname, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((hostname, port))
        sock.close()
        return True
    except socket.timeout:
        logging.error(f"Connection timeout to {hostname}")
        return False
    except ConnectionRefusedError:
        logging.error(f"Connection refused to {hostname}")
        return False
    except Exception as e:
        logging.error(f"Error connecting to {hostname}: {str(e)}")
        return False

def test_ftp_login(hostname):
    if not is_port_open(hostname, 21):
        print(f"{Fore.YELLOW}Port 21 is not open on {hostname}.{Style.RESET_ALL}")
        return False

    try:
        ftp = FTP()
        ftp.connect(hostname, timeout=3)
        ftp.login("anonymous", "anonymous")
        ftp.quit()
        return True
    except Exception as e:
        logging.error(f"FTP error on {hostname}: {str(e)}")
        return False

def print_header():
    print(Fore.CYAN + "")
    print("   FTP Login Destroyer")
    print("   Created By Joelindra")
    print(Style.RESET_ALL)

def test_ftp_login_thread(target):
    success = test_ftp_login(target)
    if success:
        print(f"{Fore.GREEN}\nFTP login successful for {target}{Style.RESET_ALL}")
        with file_lock:
            with open("vuln.txt", "a") as output_file:
                output_file.write(target + "\n")

def main():
    print_header()

    try:
        target_option = input("Choose an option:\n1. Read targets from a file\n2. Input a single target\n\nInput Here : ")

        if target_option == "1":
            file_name = input("Enter the name of the file containing target domains (one per line): ")
            target_list = []
            with open(file_name, "r") as file:
                for line in file:
                    stripped_line = line.strip()
                    if stripped_line:  # Skip blank lines
                        stripped_line = stripped_line.replace("http://", "").replace("https://", "")
                        if stripped_line.endswith("/"):
                            stripped_line = stripped_line[:-1]  # Remove trailing "/"
                        target_list.append(stripped_line)
        elif target_option == "2":
            target = input("Enter a single target hostname or IP address: ").replace("http://", "").replace("https://", "")
            if target.endswith("/"):
                target = target[:-1]  # Remove trailing "/"
            target_list = [target]
        else:
            print("Invalid option.")
            return

        threads = []

        animation_characters = "|/-\\"
        animation_index = 0
        for target in target_list:
            for i in range(10):
                print(f"{Fore.MAGENTA}{animation_characters[animation_index]}{Style.RESET_ALL}", end="\r")
                time.sleep(0.2)
                animation_index = (animation_index + 1) % 4

            thread = threading.Thread(target=test_ftp_login_thread, args=(target,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print(f"{Fore.GREEN}\nAll tests completed. Successfully logged in targets written to vuln.txt.{Style.RESET_ALL}")

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Program terminated by user.")

if __name__ == "__main__":
    main()
