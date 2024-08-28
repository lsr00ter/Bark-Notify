# Bark-CS-Notify

Cobalt Strike Beacon Notifier with [**Bark.app**](https://itunes.apple.com/cn/app/bark-customed-notifications/id1403753865)

Full credits to the author _b4r0nd3l4b1rr4_'s [Teams-CS-Notifier](https://github.com/b4r0nd3l4b1rr4/Teams-CS-Notifier)

## Usage

0. Install Bark.app, copy the server address and device key

1. Load `bark-notifier.cna` in Cobalt Strike

2. Config the notifier

3. Configure and use `headless-notifier.cna` on the teamserver

    ```
    $address_and_key = "http://api.day.app/**";
    $notification_title = "Check your teamserver!";
    ```

The script will now send a notification to the device with the Bark app installed every time a new beacon is established.

## Requirements

- Bark app installed on an iOS device
- Cobalt Strike
- Python 3

> About Bark:
> <https://github.com/Finb/bark-server>
