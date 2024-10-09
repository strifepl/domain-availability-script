import whois
import time
import requests
from datetime import datetime


def check_domain_availability(domain):
    try:
        domain_info = whois.whois(domain)
        statuses = domain_info.get('status', [])

        # Ensure statuses are in a list form
        if not isinstance(statuses, list):
            statuses = [statuses]

        # Check if the domain is in pendingDelete status
        for status in statuses:
            if 'pendingDelete' in status.lower():
                print(f"{datetime.now()}: Domain {domain} is in pendingDelete status.")
                return False
            if 'clienthold' in status.lower() or 'clienttransferprohibited' in status.lower():
                print(f"{datetime.now()}: Domain {domain} is in {status} status.")
                return False

        return True
    except Exception as e:
        print(f"{datetime.now()}: Error checking domain {domain}: {e}")
        return True


def trigger_rest_endpoint():
    endpoint_url = "https://api.gsmservice.pl/v5/send.php"
    params = {
        "login": "XXXXX",
        "pass": "XXXX",
        "recipient": "48600700800",
        "message": "Domain is available!"
    }
    try:
        response = requests.get(endpoint_url, params=params)
        response.raise_for_status()
        print(f"{datetime.now()}: REST endpoint triggered successfully!")
    except requests.exceptions.RequestException as e:
        print(f"{datetime.now()}: Failed to trigger REST endpoint: {e}")


def monitor_domain(domain):
    if check_domain_availability(domain):
        trigger_rest_endpoint()
    else:
        print(f"{datetime.now()}: Domain {domain} is not available yet. ")


if __name__ == "__main__":
    domain_to_check = "your_domain.io"
    check_interval = 3600  # Checks every hour

    monitor_domain(domain_to_check)
