import asyncio
from aiogram import Bot, Dispatcher, F, types, html
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from api import TOKEN, OWNER, CHANNEL, CHAT

# DEFINES
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Обработчики команд
@dp.message(Command('start'))
async def process_start(message: types.Message):
	if str(message.chat.id) == OWNER:
		try:
			await message.answer('Здесь будут сообщения от пользователей.')
		except Exception as ex:
			print(ex)


# Обработчики нажатий кнопок


# Обработчики сообщений
@dp.message(F.text)
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
			user_first_name_link = html.link(html.quote(message.from_user.first_name), "tg://user?id=" + str(message.from_user.id))
			await bot.send_message(OWNER, html.bold('#тейк от {user_first_name_link}')' + \n{message.text}')
			await bot.send_message(message.chat.id, f'{html.quote(message.from_user.first_name)}, ваше сообщение получено.')
		except Exception as ex:
			print(ex)


async def main():
	await dp.start_polling(bot)

if __name__ == '__main__':
	asyncio.run(main)
