**Description:**<br>
Anonymous FTP (File Transfer Protocol) is a method of accessing and retrieving files from a remote server without requiring a username or password. It's typically used to provide public access to certain files or directories, such as software updates, public data, or documents. Users can connect to the FTP server using the "anonymous" username and any email address as the password. While anonymous FTP can be a useful tool for sharing public information, it can also pose security risks if not properly configured and monitored.

**Impact:**<br>
The impact of anonymous FTP largely depends on how it's set up and what kind of files are made available. If configured correctly, it can provide easy access to public resources. However, if not properly managed, it can lead to the exposure of sensitive information, unauthorized access to private files, or even server vulnerabilities that could be exploited by malicious actors. It's important to ensure that anonymous FTP is secured and limited to only the necessary files and directories to mitigate potential risks.

**Pupose this tools**<br>
- Try to login on a ftp server using anonymous user<b>
- If the target success login, it wills stored in valid.txt file<br>

**Usage**<br>
- python3 <tools.py><br>
- Choose your decision want to exploit single target, or target on list<br>
- The target supported just url, ip, domain<br>
