from ftplib import FTP
import socket
import time

def test_ftp_login(hostname):
    try:
        ftp = FTP()
        ftp.connect(hostname, timeout=3)
        ftp.login("anonymous", "anonymous")
        ftp.quit()
        return True
    except:
        return False

def print_header():
    print("")
    print("   FTP Login Destroyer")
    print("   Created By Joelindra")
    print("")

def main():
    print_header()

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

    valid_targets = []

    for target in target_list:
        animation_characters = "|/-\\"
        for i in range(10):
            print(f"{target}... {animation_characters[i % 4]}", end="\r")
            time.sleep(0.2)

        success = test_ftp_login(target)

        if success:
            valid_targets.append(target)
            print(f"\n\033[92mFTP login successful for {target}\033[0m")
        else:
            print(f"\n\033[91mFTP login failed for {target}\033[0m")

    if valid_targets:
        with open("valid.txt", "w") as output_file:
            for target in valid_targets:
                output_file.write(target + "\n")
        print("\nValid targets written to valid.txt.")

if __name__ == "__main__":
    main()