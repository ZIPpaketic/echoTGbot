from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(Bot: bot):
    commands = [
        types.BotCommand(command='/start', description='Command to start the bot'),
        types.BotCommand(command='/help', description='Command to get help')

    ]
    await bot.set_my_commands(commands)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('q, echbot greets u')


@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Просто отправь мне любое сообщение, и я повторю его.')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup=on_startup)

