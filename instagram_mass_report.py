import requests
from bs4 import BeautifulSoup
import random
import time

# Configuration
PROXY_LIST = [
    'http://proxy1:port',
    'http://proxy2:port',
    # Add more proxies as needed
]

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    # Add more user agents as needed
]

# Instagram URLs
LOGIN_URL = 'https://www.instagram.com/accounts/login/'
REPORT_URL = 'https://www.instagram.com/report/'

# Session to maintain cookies
session = requests.Session()

# Function to get a random proxy
def get_random_proxy():
    return {'http': random.choice(PROXY_LIST), 'https': random.choice(PROXY_LIST)}

# Function to get a random user agent
def get_random_user_agent():
    return random.choice(USER_AGENTS)

# Login function
def login(username, password):
    session.headers.update({'User-Agent': get_random_user_agent()})
    session.headers.update({'Referer': LOGIN_URL})
    
    req = session.get(LOGIN_URL, proxies=get_random_proxy())
    soup = BeautifulSoup(req.content, 'html.parser')
    csrf = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
    
    login_data = {
        'username': username,
        'password': password,
        'csrfmiddlewaretoken': csrf
    }
    
    response = session.post(LOGIN_URL, data=login_data, proxies=get_random_proxy())
    if response.status_code == 200:
        print("Logged in successfully.")
    else:
        print("Failed to log in.")

# Report function
def report_account(account_id, reason='spam'):
    report_data = {
        'account_id': account_id,
        'reason': reason
    }
    
    session.headers.update({'User-Agent': get_random_user_agent()})
    response = session.post(REPORT_URL, data=report_data, proxies=get_random_proxy())
    
    if response.status_code == 200:
        print(f"Reported account {account_id} successfully.")
    else:
        print(f"Failed to report account {account_id}.")

# Mass report function for a single account
def mass_report_single_account(account_id, num_reports=10, delay=10):
    for i in range(num_reports):
        print(f"Attempting report {i+1} of {num_reports} on account {account_id}...")
        report_account(account_id)
        time.sleep(delay)  # Add delay to avoid rate limiting

# Example usage
if __name__ == "__main__":
    # Dummy account credentials
    USERNAME = 'your_dummy_username'
    PASSWORD = 'your_dummy_password'
    
    # Target account ID for mass reporting
    TARGET_ACCOUNT_ID = 'target_dummy_account_id'
    
    # Number of reports to perform
    NUM_REPORTS = 10  # Adjust as needed
    DELAY_BETWEEN_REPORTS = 10  # Delay in seconds
    
    # Login
    login(USERNAME, PASSWORD)
    
    # Perform mass reporting on the single account
    mass_report_single_account(TARGET_ACCOUNT_ID, num_reports=NUM_REPORTS, delay=DELAY_BETWEEN_REPORTS)