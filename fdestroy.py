from ftplib import FTP
import socket
import time
import threading
import logging
import itertools
from colorama import Fore, Style, init
from concurrent.futures import ThreadPoolExecutor, as_completed

# Initialize colorama
init()

# Lock for thread-safe file access
file_lock = threading.Lock()

# Initialize logger
logging.basicConfig(filename='error.log', level=logging.ERROR)

# Global flag for stopping the animation
animation_active = True

def is_port_open(hostname, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((hostname, port))
        sock.close()
        return True
    except socket.timeout:
        logging.error(f"Connection timeout to {hostname}")
        print(f"{Fore.RED}[!] Timeout: Unable to connect to {hostname} on port {port}{Style.RESET_ALL}")
        return False
    except ConnectionRefusedError:
        logging.error(f"Connection refused to {hostname}")
        print(f"{Fore.RED}[!] Connection refused: {hostname} on port {port}{Style.RESET_ALL}")
        return False
    except Exception as e:
        logging.error(f"Error connecting to {hostname}: {str(e)}")
        print(f"{Fore.RED}[!] Error connecting to {hostname}: {str(e)}{Style.RESET_ALL}")
        return False

def test_ftp_login(hostname, username="anonymous", password="anonymous"):
    if not is_port_open(hostname, 21):
        return False

    try:
        ftp = FTP()
        ftp.connect(hostname, timeout=3)
        ftp.login(username, password)
        ftp.quit()
        return True
    except Exception as e:
        logging.error(f"FTP error on {hostname}: {str(e)}")
        print(f"{Fore.RED}[!] FTP error on {hostname}: {str(e)}{Style.RESET_ALL}")
        return False

def print_header():
    print(Fore.CYAN + Style.BRIGHT)
    print("   ╔═════════════════════════════╗")
    print("   ║       FTP Login Destroyer   ║")
    print("   ║       Created by Joelindra  ║")
    print("   ╚═════════════════════════════╝")
    print(Style.RESET_ALL)

def test_ftp_login_thread(target):
    success = test_ftp_login(target)
    if success:
        print(f"{Fore.GREEN}[+] FTP login successful for {target}{Style.RESET_ALL}")
        with file_lock:
            with open("vuln.txt", "a") as output_file:
                output_file.write(target + "\n")

def animate_progress():
    global animation_active
    animation_characters = "|/-\\"
    for frame in itertools.cycle(animation_characters):
        if not animation_active:
            break
        print(f"{Fore.MAGENTA}{frame}{Style.RESET_ALL}", end="\r")
        time.sleep(0.1)

def main():
    global animation_active
    print_header()

    try:
        print(f"{Fore.YELLOW}[*] Choose an option:{Style.RESET_ALL}")
        target_option = input(f"{Fore.LIGHTCYAN_EX}1. Read targets from a file\n2. Input a single target\n\n{Fore.LIGHTGREEN_EX}Input Here: {Style.RESET_ALL}")

        # Initialize target list based on user input
        target_list = []
        
        if target_option == "1":
            file_name = input(f"{Fore.LIGHTCYAN_EX}Enter the name of the file containing target domains (one per line): {Style.RESET_ALL}")
            try:
                with open(file_name, "r") as file:
                    target_list = [line.strip().replace("http://", "").replace("https://", "").rstrip("/") for line in file if line.strip()]
            except FileNotFoundError:
                print(f"{Fore.RED}[!] Target file {file_name} not found.{Style.RESET_ALL}")
                return
        elif target_option == "2":
            target = input(f"{Fore.LIGHTCYAN_EX}Enter a single target hostname or IP address: {Style.RESET_ALL}").replace("http://", "").replace("https://", "").rstrip("/")
            target_list = [target]
        else:
            print(f"{Fore.RED}[!] Invalid option.{Style.RESET_ALL}")
            return

        # Start the animation in a separate thread
        animation_thread = threading.Thread(target=animate_progress)
        animation_thread.start()

        # Use a thread pool to handle multiple targets efficiently
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            for target in target_list:
                futures.append(executor.submit(test_ftp_login_thread, target))

            # Wait for all tasks to complete
            for future in as_completed(futures):
                pass

        # Stop the animation once all tasks are done
        animation_active = False
        animation_thread.join()

        print(f"{Fore.GREEN}[+] All tests completed. Check 'vuln.txt' for results.{Style.RESET_ALL}")

    except KeyboardInterrupt:
        animation_active = False
        animation_thread.join()
        print(f"\n{Fore.RED}[!] Program terminated by user.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
