# Instagram-Mass-Reporting-Tool



# Instagram Mass Reporting Tool (Educational Purposes Only)

This repository contains a Python script designed to simulate mass reporting on a single Instagram account. The tool is intended for **educational purposes only** and should be used responsibly, with proper authorization.

---

## Table of Contents
1. [Disclaimer](#disclaimer)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Configuration](#configuration)
7. [Ethical Considerations](#ethical-considerations)
8. [License](#license)

---

## Disclaimer

This tool is for **educational purposes only**. It is designed to help cybersecurity professionals and researchers understand how automated reporting systems work. Unauthorized use of this tool to harass, target, or harm individuals or accounts is strictly prohibited and may violate Instagram's terms of service and local laws. The developer is not responsible for any misuse of this tool.

---

## Features

- **Single Account Targeting**: Focuses on repeatedly reporting a single Instagram account.
- **Proxy Rotation**: Uses a list of proxies to simulate requests from different IP addresses.
- **User-Agent Rotation**: Randomly selects user agents to mimic different browsers.
- **Rate Limiting**: Introduces a delay between reports to avoid triggering Instagram’s anti-abuse mechanisms.
- **CSRF Token Handling**: Automatically handles CSRF tokens required for login.

---

## Prerequisites

Before using this tool, ensure you have the following:

1. **Python 3.x**: Install Python from [python.org](https://www.python.org/).
2. **Required Libraries**: Install the required Python libraries using pip:
   ```bash
   pip install requests beautifulsoup4
   ```
3. **Dummy Instagram Account**: Create a dummy Instagram account for testing purposes.
4. **Proxies**: Obtain a list of proxies to rotate IP addresses (optional but recommended).

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/instagram-mass-reporting-tool.git
   cd instagram-mass-reporting-tool
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Configure the Script**:
   - Open the script (`instagram_mass_report.py`) and update the following variables:
     - `USERNAME`: Your dummy Instagram account username.
     - `PASSWORD`: Your dummy Instagram account password.
     - `TARGET_ACCOUNT_ID`: The account ID of the target account (for educational purposes only).
     - `NUM_REPORTS`: The number of reports to send.
     - `DELAY_BETWEEN_REPORTS`: The delay (in seconds) between each report.

2. **Run the Script**:
   ```bash
   python instagram_mass_report.py
   ```

3. **Monitor Output**:
   - The script will log the progress of each report in the terminal.

---

## Configuration

### Proxy List
Add your proxies to the `PROXY_LIST` in the script:
```python
PROXY_LIST = [
    'http://proxy1:port',
    'http://proxy2:port',
    # Add more proxies as needed
]
```

### User Agents
Add or modify user agents in the `USER_AGENTS` list:
```python
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    # Add more user agents as needed
]
```

---

## Ethical Considerations

- **Authorization**: Only use this tool on accounts you own or have explicit permission to test.
- **Compliance**: Ensure your actions comply with Instagram's terms of service and local laws.
- **Transparency**: Clearly state the purpose of your testing and avoid any malicious intent.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

---

## Support

If you find this project useful, consider giving it a ⭐️ on GitHub! For questions or feedback, feel free to open an issue.
