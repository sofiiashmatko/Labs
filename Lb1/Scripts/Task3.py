import asyncio
from telethon import TelegramClient
from telethon.tl.types import User

API_ID =
API_HASH = ''
SESSION_NAME = 'my_session_name'


async def main():
    async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:

        await client.send_message('me', 'Tест самому собі!')
        print("Повідомлення в Saved Messages відправлено.")

        try:
            await client.send_message('@bshdiskwnhfu', 'Привіт, це Я!')
            print("Повідомлення для @bshdiskwnhfu відправлено.")
        except Exception as e:
            print(f"Не вдалося відправити повідомлення для @some_username: {e}")

        chat_username = '@sos_kharkiv21'

        try:
            print(f"\nОтримання перших учасників з '{chat_username}'...")

            count = 0
            async for user in client.iter_participants(chat_username, limit=20):
                if isinstance(user, User):
                    print(f"  - ID: {user.id}, Ім'я: {user.first_name}, @{user.username}")
                    count += 1

            print(f"Показано перших {count} учасників.")

        except Exception as e:
            print(f"Не вдалося отримати учасників з '{chat_username}': {e}")


if __name__ == '__main__':
    asyncio.run(main())