# Bark-CS-Notify

Cobalt Strike Beacon Notify version in **Bark.app** using Webhook

> 使用 Webhook 的 **Bark.app** 版 Cobalt Strike Beacon Notify

Full credits to the author _b4r0nd3l4b1rr4_'s [Teams-CS-Notifier](https://github.com/b4r0nd3l4b1rr4/Teams-CS-Notifier)

> 感谢原作者 _b4r0nd3l4b1rr4_ 的 [Teams-CS-Notifier](https://github.com/b4r0nd3l4b1rr4/Teams-CS-Notifier)

## Using:

> ## 使用方法：

1. Modify the `notify.py` file to pull your or your team's device key into `DEVICE_KEY_LIST`, or change `BARK_SERVER` if you want.

   > 1. 修改 `notify.py` 文件，将你或你的团队的设备密钥拉入 `DEVICE_KEY_LIST`，或者如果你想改变 `BARK_SERVER` 。

2. Open your Cobalt Strike

   > 2. 打开你的 Cobalt Strike

3. Go to `Cobalt Strike > Script Manager`

   > 3. 转到 `Cobalt Strike > Script Manager`

4. Add the `barknotify.cna` file
   > 4. 添加 `barknotify.cna` 文件

The script will now send a notification to the bark-installed device every time a new beacon is established.

> 现在，每次新主机上线时，脚本都会向安装了 Bark.app 的设备发送通知。

## Requirements

- Cobalt Strike
- Python 3
- Requests module (`pip install requests`)

> About Bark app:
> https://github.com/Finb/bark-server
