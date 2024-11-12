from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hlink
from aiogram.dispatcher.filters import Text
from api import TOKEN, OWNER, CHANNEL, CHAT
import re
import config

# DEFINES
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# Создание кнопок для меню


# Обработчик команд
@dp.message_handler(commands='start')
async def process_start(message: types.Message):
	if str(message.chat.id) == OWNER:
		try:
			await message.answer('Здесь будут сообщения от пользователей.')
		except Exception as ex:
			print(ex)

@dp.message_handler(commands='ping')
async def process_ping(message: types.Message):
	await message.answer('PONG!')

# Обработчик нажатий кнопок


# Обработчик сообщений
@dp.message_handler()
async def messages(message: types.Message):
	if str(message.chat.id) == OWNER:
		if message.reply_to_message:
			try:
				message_data = message.reply_to_message.text
				original_user_id = re.findall('UID: [0-9]+', message_data)[0].replace('UID: ', '').strip()
				original_message_id = re.findall('MID: [0-9]+', message_data)[0].replace('MID: ', '').strip()
				await bot.send_message(original_user_id, message.text, reply_to_message_id=original_message_id, allow_sending_without_reply=True)
				text = f'Ваш ответ пользователю {original_user_id} отправлен.'
				await bot.send_message(OWNER, text)
			except Exception as ex:
				print(ex)
	else:
		try:
			await bot.send_message(OWNER, f'<b>#тейк от {hlink(message.from_user.first_name, "tg://user?id=" + str(message.from_user.id))}</b> \n {message.text}')
			await bot.send_message(message.chat.id, f'{message.from_user.first_name}, ваше сообщение получено.')
		except Exception as ex:
			print(ex)


if __name__ == '__main__':
	executor.start_polling(dp)
