from telethon import TelegramClient, events
from telethon.tl.functions.messages import SetTypingRequest
from telethon.tl.types import SendMessageTypingAction
import asyncio

api_id = 24523420
api_hash = '67674fbe96c797365264f03d5e67847e'
session_name = 'my_userbot_session'

client = TelegramClient(session_name, api_id, api_hash)

responded_users = set()

first_message = "Приветик, я могу подарить подарок за 350 ⭐️, осталось всего 48 штучек. Но есть задание"

second_message = (
    '1) Лайкни и напиши "спасибо" под комментарием с которого узнали обо мне!\n\n'
    '2) Напиши под 10 любых видео этот текст ⬇️\n\n'
    '<code>Давайте, всем по колечку дарю @flowy69 💍</code>\n\n'
    '‼️ ОБЯЗАТЕЛЬНО ЛАЙКАЙТЕ ВСЕ СВОИ КОММЕНТЫ‼️\n\n'
    'Когда будет готово не забудь скинуть скрины, все проверю!!!'
)

third_message = "И последнее, подпишись на канал, где я ежедневно провожу бесплатные раздачи подарков) @Flowy"

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if not event.is_private or event.out:
        return

    user_id = event.sender_id

    # Если это фото, и бот ещё не отвечал
    if event.photo and user_id in responded_users:
        await client(SetTypingRequest(peer=event.chat_id, action=SendMessageTypingAction()))
        await asyncio.sleep(5)
        await client.send_message(event.chat_id, third_message)
        return

    # Если уже отвечали — игнорируем
    if user_id in responded_users:
        return

    responded_users.add(user_id)

    try:
        # Печатает 7 секунд перед первым сообщением
        await client(SetTypingRequest(peer=event.chat_id, action=SendMessageTypingAction()))
        await asyncio.sleep(7)
        await client.send_message(event.chat_id, first_message)

        # Печатает ещё 7 секунд перед вторым сообщением
        await client(SetTypingRequest(peer=event.chat_id, action=SendMessageTypingAction()))
        await asyncio.sleep(7)
        await client.send_message(event.chat_id, second_message, parse_mode='html')

    except Exception as e:
        print("Handler error:", e)

print("Бот запущен...")
client.start()
client.run_until_disconnected()
