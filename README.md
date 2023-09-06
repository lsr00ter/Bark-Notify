# Bark-CS-Notify

Cobalt Strike Beacon Notify version in **Bark.app** using Webhook

> 使用 Webhook 的 **Bark.app** 版 Cobalt Strike Beacon Notify

Full credits to the author _b4r0nd3l4b1rr4_'s [Teams-CS-Notifier](https://github.com/b4r0nd3l4b1rr4/Teams-CS-Notifier)

> 感谢原作者 _b4r0nd3l4b1rr4_ 的 [Teams-CS-Notifier](https://github.com/b4r0nd3l4b1rr4/Teams-CS-Notifier)

## Using:

> ## 使用方法：

0. Install Bark.app and get your device key, The device key shows at `https://$Server/**$device_key**/`

   > 0. 安装 Bark.app 获取 device key, Device key 在 `https://$Server/**$device_key**/` 位置。

1. Modify the `notify.py` file to pull your or your team member's device key into `DEVICE_KEY_LIST`, or change `BARK_SERVER` if you want.

   > 1. 修改 `notify.py` 文件，将你或你的团队成员的设备密钥拉入 `DEVICE_KEY_LIST`，或者修改私有化部署的 `BARK_SERVER` 。

2. Open your Cobalt Strike

   > 2. 打开你的 Cobalt Strike

3. Go to `Cobalt Strike > Script Manager`

   > 3. 转到 `Cobalt Strike > Script Manager`

4. Add the `barknotify.cna` file
   > 4. 添加 `barknotify.cna` 文件

The script will now send a notification to the bark-installed device every time a new beacon is established.

> 现在，每次新主机上线时，脚本都会向安装了 Bark.app 的设备发送通知。

## Requirements

- Bark app installed
- Cobalt Strike
- Python 3
- Requests module (`pip install requests`)

> About Bark app:
> https://github.com/Finb/bark-server
