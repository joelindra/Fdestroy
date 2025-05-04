# FTP Login Destroyer 2.0

![Python](https://img.shields.io/badge/python-3.8%2B-blue)

An advanced FTP security scanning tool designed to identify vulnerable FTP servers with weak authentication. The tool tests anonymous login capability and provides detailed reports on successful connections.

## 🔍 Features

- **Multi-threaded scanning**: Test multiple targets concurrently for efficient scanning
- **Anonymous FTP login detection**: Identify servers allowing anonymous access
- **Rich interactive UI**: Beautiful terminal interface with real-time statistics
- **Comprehensive reporting**: Detailed HTML reports with server information
- **File browsing capabilities**: View sample files on vulnerable servers
- **Robust error handling**: Graceful handling of connection issues
- **Progress tracking**: Real-time progress with estimated completion time

## 📋 Requirements

- Python 3.8 or higher
- Required Python packages:
  ```
  rich>=10.9.0
  ```

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/joelindra/fdestroy.git
cd Fdestroy

# Install dependencies
pip install -r requirements.txt
```

## 💻 Usage

### Basic Usage

```bash
# Scan a single target
python fdestroy.py -t example.com

# Scan multiple targets from a file
python festroy.py -l targets.txt
```

### Command Line Options

| Option | Description |
|--------|-------------|
| `-t, --target` | Single target hostname or IP |
| `-l, --list` | File containing target list (one per line) |
| `-w, --workers` | Number of concurrent workers (default: 20) |
| `-o, --output` | Output file for vulnerable targets (default: vuln.txt) |
| `--timeout` | Connection timeout in seconds (default: 3) |

## 📊 Output

The tool generates two types of output:
1. A text file (`vuln.txt` by default) containing vulnerable hosts
2. An HTML report with detailed information about each scanned target

![image](https://github.com/user-attachments/assets/1b6770e8-6199-4529-a2c6-033477c6befb)

### Sample HTML Report
The HTML report includes:
- Scan statistics
- Details of successful connections
- Banner information
- System type
- Initial directory
- Sample files (if available)
- Failed connection attempts with error details

## ⚠️ Legal Disclaimer

This tool is provided for educational and ethical security research purposes only. Usage of FTP Login Destroyer for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. The developers assume no liability and are not responsible for any misuse or damage caused by this program.

## 🔒 Security Recommendations

If your server is found vulnerable by this tool, consider implementing the following security measures:

1. Disable anonymous FTP access if not required
2. Implement strong password policies
3. Use FTP over SSL/TLS (FTPS) or SFTP instead of plain FTP
4. Configure proper access controls and file permissions
5. Implement IP-based access restrictions
6. Enable logging and monitoring for FTP services

## 🛠️ Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Rich](https://github.com/Textualize/rich) - Beautiful terminal formatting
- Security researchers who contributed to FTP vulnerability research
