import http.client
import urllib.parse
import sys
import json

# import base64
# import requests


def send_notification(
    title, external_ip, internal_ip, computer_name, username, address_and_key
):
    """
    This function sends a notification to a specified address and key.

    Parameters:
    title (str): The title of the notification.
    external_ip (str): The external IP address of the computer.
    internal_ip (str): The internal IP address of the computer.
    computer_name (str): The name of the computer.
    username (str): The username of the user.
    address_and_key (str): The address and key to send the notification to.

    Returns:
    int: The status code of the HTTP request.
    """

    notify_body = f"New beacon: {username}@{internal_ip} ({computer_name})"
    if address_and_key.startswith("http"):
        base_url = (
            address_and_key.split("/")[0]
            + "//"
            + address_and_key.split("/")[2]
            + "/push"
        )
        key = address_and_key.split("/")[3]
    else:
        sys.exit()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    payload = {
        "title": title,
        "body": notify_body,
        "device_key": key,
        "level": "timeSensitive",
        "badge": 1,
        # "sound": "minuet.caf",
        # Cobalt Strike logo for push notification display
        # "icon": "https://www.kali.org/tools/armitage/images/armitage-logo.svg",
        "icon": "https://img2.baidu.com/it/u=2228721569,336857378&fm=253&fmt=auto&app=138&f=JPEG?w=320&h=320",
        "group": "CobaltStrike Notification",
        # 点开通知后打开的 URL
        # "url": "https://github.com",
    }
    try:
        json.loads(json.dumps(payload))
    except ValueError as e:
        print(f"Invalid JSON: {e}")
        sys.exit()
    parsed_url = urllib.parse.urlparse(base_url)
    conn = http.client.HTTPSConnection(parsed_url.netloc)
    try:
        conn.request("POST", parsed_url.path, json.dumps(payload), headers)
        response = conn.getresponse()
        return response.status
    finally:
        conn.close()


if __name__ == "__main__":
    # $command = @('python3', $PythonScriptPath, $notification_title, $computer, $internal, $external, $user, $address_and_key);
    notification_title = sys.argv[1]
    computer_name = sys.argv[2]
    internal_ip = sys.argv[3]
    external_ip = sys.argv[4]
    username = sys.argv[5]
    address_and_key = sys.argv[6]
    send_notification(
        notification_title,
        external_ip,
        internal_ip,
        computer_name,
        username,
        address_and_key,
    )
