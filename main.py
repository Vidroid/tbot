#!venv/bin/python
import logging
import conf

from aiogram import Bot, Dispatcher, executor, types

# Объект бота
bot = Bot(token=conf.TOKEN, parse_mode='HTML')
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Хэндлер на команду /test1
@dp.message_handler()
async def cmd_test1(message: types.Message):

    if message.chat.id == conf.PIN:
        #-1001579740736
        if message.text.lower() == 'pcast h':
            if message.reply_to_message:
                msg = await bot.send_message(conf.HIGH, message.reply_to_message.text)
                await bot.pin_chat_message(conf.HIGH, msg.message_id)
                await bot.send_message(conf.PIN, 'Done to H')

        if message.text.lower() == 'pcast w':
            if message.reply_to_message:
                msg = await bot.send_message(conf.LAMP, message.reply_to_message.text)
                await bot.pin_chat_message(conf.LAMP, msg.message_id)
                await bot.send_message(conf.PIN, 'Done to Lamp')

        if message.text.lower() == 'pcast t':
            if message.reply_to_message:
                msg = await bot.send_message(conf.TOP, message.reply_to_message.text)
                await bot.pin_chat_message(conf.TOP, msg.message_id)
                await bot.send_message(conf.PIN, 'Done to T')

        if message.text.lower() == 'pcast a':
            if message.reply_to_message:
                await bot.unpin_all_chat_messages(conf.LAMP)
                msg = await bot.send_message(conf.LAMP, message.reply_to_message.text)
                await bot.pin_chat_message(conf.LAMP, msg.message_id)
                await bot.unpin_all_chat_messages(conf.TOP)
                msg2 = await bot.send_message(conf.TOP, message.reply_to_message.text)
                await bot.pin_chat_message(conf.TOP, msg2.message_id)
                await bot.unpin_all_chat_messages(conf.HIGH)
                msg3 = await bot.send_message(conf.HIGH, message.reply_to_message.text)
                await bot.pin_chat_message(conf.HIGH, msg3.message_id)
                await bot.send_message(conf.PIN, 'Done to ALL')

        if message.text.lower() == 'ncast h':
            if message.reply_to_message:
                msg = await bot.send_message(conf.HIGH, message.reply_to_message.text)
                await bot.send_message(conf.PIN, 'Done to H')

        if message.text.lower() == 'ncast w':
            if message.reply_to_message:
                msg = await bot.send_message(conf.LAMP, message.reply_to_message.text)
                await bot.send_message(conf.PIN, 'Done to Lamp')

        if message.text.lower() == 'ncast t':
            if message.reply_to_message:
                msg = await bot.send_message(conf.TOP, message.reply_to_message.text)
                await bot.send_message(conf.PIN, 'Done to T')

        if message.text.lower() == 'ncast a':
            if message.reply_to_message:
                msg = await bot.send_message(conf.LAMP, message.reply_to_message.text)
                msg2 = await bot.send_message(conf.TOP, message.reply_to_message.text)
                msg3 = await bot.send_message(conf.HIGH, message.reply_to_message.text)
                await bot.send_message(conf.PIN, 'Done to ALL')

    if message.from_user.id == conf.ME:
        if message.text.lower() == 'дайид':
            await bot.send_message(message.chat.id, message.chat.id)

    if message.from_user.id == conf.ME:
        if message.text.lower() == 'алтарь':
            await bot.send_dice(message.chat.id)

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)