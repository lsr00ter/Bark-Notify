import sys
import json
import base64
import requests


BARK_SERVER = "http://api.day.app/push"
DEVICE_KEY_LIST = [""]


def send_notification(
    title, external_ip, internal_ip, hostname, username, BARK_SERVER, key
):
    notify_body = "; ".join(
        [
            "New Beacon from:" + external_ip,
            "Internal_IP:" + internal_ip,
            "Host.name:" + hostname,
            "User.name:" + username,
        ]
    )
    headers = {"Content-Type": "application/json; charset=utf-8"}
    payload = {
        "title": title,
        "body": notify_body,
        "device_key": key,
        "level": "timeSensitive",
        "badge": 1,
        # "sound": "minuet.caf",
        # Cobalt Strike logo for push notification display
        "icon": "https://www.aldeid.com/w/images/8/83/Armitage-logo.png",
        "group": "CobaltStrike 上线提醒",
        # 点开链接后打开的 URL
        # "url": "https://github.com",
    }
    try:
        json.loads(json.dumps(payload))
    except ValueError as e:
        print(f"Invalid JSON: {e}")

    response = requests.post(BARK_SERVER, headers=headers, data=json.dumps(payload))
    # print(response.status_code)
    return response.status_code


if __name__ == "__main__":
    title = sys.argv[1]
    external_ip = sys.argv[2].split(":")[1].strip()
    internal_ip = sys.argv[3].split(":")[1].strip()
    hostname = sys.argv[4].split(":")[1].strip()
    username = sys.argv[5].split(":")[1].strip()
    for key in DEVICE_KEY_LIST:
        send_notification(
            title, external_ip, internal_ip, hostname, username, BARK_SERVER, key
        )
