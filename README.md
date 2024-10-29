# Inj3ctify

## Overview
**Inj3ctify** is an automated Python-based SQL injection tool designed to help ethical hackers and penetration testers identify and exploit SQL injection vulnerabilities in web applications. **Use responsibly and for legal purposes only.**

## Features
- Automated injection scanning for GET/POST requests  
- Supports common SQL injection payloads  
- Customizable options for targeting specific parameters  
- Detects different SQL database engines (MySQL, PostgreSQL, etc.)  
- Easy to extend and integrate with other tools  

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/tanveen06/inj3ctify.git
   cd inj3ctify
   ```

2. Ensure Python 3.x is installed on your system:
   ```bash
   python --version
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the tool with:
```bash
python Inj3ctify.py --url <target_url> --param <vulnerable_param>
```

### Example:
```bash
python  Inj3ctify.py --url "http://example.com/index.php?id=1" --param "id"
```

### Options:
| **Argument**     | **Description**                         |
|------------------|-----------------------------------------|
| `--url`          | Target URL with vulnerable parameter    |
| `--param`        | Parameter to test for SQL injection     |
| `--verbose`      | Enable verbose output                   |
| `--help`         | Show help message                       |

## Disclaimer
This tool is intended for educational purposes and ethical testing on systems with proper authorization. **Using it on unauthorized systems is illegal.** The author is not responsible for any misuse or damage caused.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing
Contributions are welcome! Feel free to submit pull requests or open issues for feature requests or bug reports.

## Acknowledgements
Special thanks to the open-source community for their contributions and inspiration in creating this tool.
