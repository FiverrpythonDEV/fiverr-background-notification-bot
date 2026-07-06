# Fiverr Background Notification Bot 🚀

An enterprise-ready, asynchronous Python Telegram bot engineered to track Fiverr inquiry updates and order notifications in real-time. This project is built to run 24/7 as a native Linux background daemon (`systemd`), featuring automated crash recovery and secure token management.

---

## ✨ Features

* **Asynchronous Architecture:** Utilizing `aiogram 3.x` and `aiohttp` for high-performance, non-blocking operation loops.
* **Smart Monitoring:** Simulates secure browser HTTP communication via session cookies to fetch updates efficiently.
* **Production Deployment:** Runs as a standard background system daemon (`systemd` service). It boots automatically with your machine (even before user login) and includes a 5-second auto-restart policy in case of network drops.
* **Secure by Design:** Zero hardcoded credentials. All sensitive session configuration data and Telegram API keys are strictly parsed through environment variables (`os.environ`).

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** Aiogram 3.x (Asynchronous Telegram Bot API)
* **HTTP Client:** Aiohttp
* **Environment:** Arch Linux / Debian-based systems
* **Process Manager:** Systemd

---

## ⚙️ Project Structure

```text
fiverr-background-notification-bot/
├── main.py          # Main asynchronous bot engine & web-scraping logic
├── .gitignore       # Protection file ensuring no local tokens are committed
├── LICENSE          # MIT Open Source License
└── README.md        # Comprehensive system documentation

🚀 Installation & Deployment
1. Clone the repository
Bash

git clone [https://github.com/FiverrpythonDEV/fiverr-background-notification-bot.git](https://github.com/FiverrpythonDEV/fiverr-background-notification-bot.git)
cd fiverr-background-notification-bot

2. Configure Environment Variables

Create a persistent environment file or pass variables to your runtime environment:
Bash

export BOT_TOKEN="your_telegram_bot_token"
export CHAT_ID="your_telegram_chat_id"
export FIVERR_COOKIE="your_secure_fiverr_session_cookie"

3. Setup Systemd Daemon (24/7 Background Run)

To ensure the script runs non-stop without keeping a terminal open, deploy it as a system service:

    Create a service file:
    Bash

    sudo nano /etc/systemd/system/fiverr_bot.service

    Paste the configuration:
    Ini, TOML

    [Unit]
    Description=Fiverr Background Notification Bot Daemon
    After=network.target

    [Service]
    Type=simple
    User=root
    WorkingDirectory=/path/to/your/bot
    ExecStart=/usr/bin/python3 /path/to/your/bot/main.py
    Restart=always
    RestartSec=5
    Environment="BOT_TOKEN=your_token" "CHAT_ID=your_id" "Fiverr_COOKIE=your_cookie"

    [Install]
    WantedBy=multi-user.target

    Enable and start the daemon:
    Bash

    sudo systemctl daemon-reload
    sudo systemctl enable fiverr_bot.service
    sudo systemctl start fiverr_bot.service

4. Check Runtime Logs

To monitor the system execution and verify the web scraping loops:
Bash

journalctl -u fiverr_bot.service -n 20 --no-pager

📄 License

This project is licensed under the MIT License — feel free to modify, distribute, and use it for commercial or personal automation workflows.



