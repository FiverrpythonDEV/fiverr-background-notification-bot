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
