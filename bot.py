import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from datetime import datetime
from utils import check_upbit_signals
from apscheduler.schedulers.asyncio import AsyncIOScheduler

API_TOKEN = "7683066723:AAHot2507_9RrkpNCMh5QKLi0cQr7cPEVH8"
CHAT_ID = "5305138065"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer("👋 Бот работает! Буду присылать сигналы по возможным листингам на Upbit.")

async def notify_work():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await bot.send_message(CHAT_ID, f"🤖 Бот работает. Время: {now}")

async def check_upbit_candidates():
    candidates = await check_upbit_signals()
    if candidates:
        msg = "🚨 Возможные листинги на Upbit:\n" + "\n".join([f"- {c}" for c in candidates])
        await bot.send_message(CHAT_ID, msg)

async def main():
    scheduler.add_job(notify_work, "interval", hours=5)
    scheduler.add_job(check_upbit_candidates, "interval", minutes=60)
    scheduler.start()
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())