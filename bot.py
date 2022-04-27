from aiogram import Bot, Dispatcher,executor,types
from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands="start")
async def start(mesasage:types.Message):
    await mesasage.reply("kakie novosti?")

if __name__=="__main__":
    executor.start_polling(dp)