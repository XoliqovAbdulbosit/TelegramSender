import asyncio
import aiohttp
import os

TOKEN = ""
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"
current_directory = os.getcwd()

lst = []

async def send_photo_with_caption(chat_id, photo, caption):
    url = f"{BASE_URL}/sendPhoto"
    img = os.path.join(current_directory, photo)
    data = aiohttp.FormData()
    data.add_field('chat_id', str(chat_id))
    data.add_field('photo', open(img, 'rb'))
    data.add_field('caption', caption)
    data.add_field('parse_mode', "Markdown")
    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.post(url, data=data) as response:
            if response.status == 200:
                return True
            else:
                error_text = await response.text()
                print(error_text)

text = """"""
errors = []

async def main():
    print(text)
    verify = input("Verify? (y/n): ")
    if verify == "n":
        exit(0)
    else:
        for id in lst:
            try:
                status = await send_photo_with_caption(id, "photo.jpeg", text)
                if status:
                    print(f"Success: {id}")
                else:
                    print(f"Error: {id}")
            except:
                errors.append(id)
                print(f"Error: {id}")

if __name__ == '__main__':
    asyncio.run(main())
    print(errors)
