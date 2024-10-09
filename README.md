# Domain Availability Monitor

This Python script checks the availability of a specific domain and triggers a REST endpoint to send a notification if the domain is available. The script runs periodically, checking the domain status at a specified interval.

## Features

- Checks the availability of a domain using the `whois` module.
- Identifies if the domain is in `pendingDelete`, `clientHold`, or `clientTransferProhibited` status.
- Triggers a REST API endpoint to notify via SMS if the domain is available.

## Requirements

- Python 3.x
- Required Python libraries:
  - `whois`
  - `requests`

You can install the necessary dependencies using the following command:

```bash
pip install python-whois requests
```

## Usage

1. Clone or download the repository.
2. Install the required dependencies.
3. Open the `main.py` file and update the following values in the `trigger_rest_endpoint()` function:
   - `login`: Your API login credentials.
   - `pass`: Your API password.
   - `recipient`: The phone number to receive the SMS notification (in international format).
   - `message`: The message to send when the domain is available.
4. Update the `domain_to_check` variable in the `__main__` section with the domain you want to monitor.
5. Adjust the `check_interval` variable to set the desired check frequency (in seconds). The default is 3600 seconds (1 hour).

### Example

To monitor the domain `your_domain.io` every hour, you can run the script like this:

```bash
python main.py
```

## How it Works

1. The script uses the `whois` module to check the domain's current status.
2. If the domain is not in `pendingDelete`, `clientHold`, or `clientTransferProhibited` status, it is considered available.
3. Once the domain is available, the script triggers the specified REST API endpoint to send an SMS notification.
4. The script runs periodically, checking the domain status at the defined interval.

## Error Handling

- The script catches and logs exceptions during the domain status check and REST API call, ensuring that errors don't interrupt the monitoring process.

## License

This project is open source and available under the [MIT License](LICENSE).
