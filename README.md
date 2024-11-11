# Channel Posting Bot:
Телеграм бот позволяющий получать сообщения, редактировать их а в последствии постить в канал.

## Установка и запуск:
1. `https://github.com/Void-Owl-Studio/tg-channel-bot.git, to clone the repository.
2. `cd tg-channel-bot`, чтобы перейти в папку проекта.
3. Установите зависимости введя `pip3 install -r requirements.txt`.
4. Отредактируйте `config.ini`
   > - TOKEN = ''   # Токен Телеграм-бота
   > - OWNER = ''   # ID чата администратора бота (кто будет видеть запросы от пользователей)
   > - CHANNEL = '' # ID канала для поста
   > - Получить TOKEN можно тут: @BotFather
5. Запустить используя `python3.8 main.py`, остановить нажам сочетание <kbd>CTRL</kbd>+<kbd>C</kbd>.
