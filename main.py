import asyncio
import logging
import os
import sys
import aiohttp
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# SECURITY NOTE: Real tokens are loaded via environment variables for security.
# Fallback strings are placeholders for GitHub portfolio.
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN_HERE")
SESSION_COOKIE = os.environ.get("FIVERR_SESSION_COOKIE", "YOUR_FIVERR_SESSION_COOKIE_HERE")
CHAT_ID = None

dp = Dispatcher()
LAST_COUNT = 0

async def check_fiverr_notifications():
    url = "https://www.fiverr.com/conversations"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json"
    }
    cookies = {
        "_fiverr_session": SESSION_COOKIE
    }
    
    try:
        async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("unread_count", 0)
                elif response.status == 401:
                    logging.error("Fiverr session expired or invalid.")
                    return -2
                return 0
    except Exception as e:
        logging.error(f"Scraping error: {e}")
        return -1

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    global CHAT_ID
    CHAT_ID = message.chat.id
    await message.answer(
        f"Hello, {html.bold(message.from_user.full_name)}.\n\n"
        f"Fiverr Web Scraping Monitor Active.\n"
        f"Automated background tracking has been initiated for your account."
    )

async def global_monitor_loop(bot: Bot):
    global LAST_COUNT
    while True:
        await asyncio.sleep(60)
        if CHAT_ID is None:
            continue
            
        current_count = await check_fiverr_notifications()
        
        if current_count > 0 and current_count > LAST_COUNT:
            new_msg = current_count - LAST_COUNT
            try:
                await bot.send_message(
                    chat_id=CHAT_ID,
                    text=f"Notification: You have {new_msg} new unread discussion(s) on Fiverr."
                )
            except Exception as e:
                logging.error(f"Failed to alert user: {e}")
        
        if current_count >= 0:
            LAST_COUNT = current_count

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    asyncio.create_task(global_monitor_loop(bot))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
