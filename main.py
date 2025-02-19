import random
from utils import *
from config import *
from scrapper import Scrapper
import asyncio

async def main():
    scrapper = Scrapper(proxy=PROXY)

    with open('wallets.txt', 'r') as f:
        wallets = f.read().splitlines()

    for wallet in wallets:
        wallet_data = await scrapper.balance(wallet)  # Получение данных для кошелька
        print(wallet_data)
        # Смена IP
        if PROXY:
            q = await change_ip(CHANGE_IP_LINK)
            print(f'Changing IP: {q}')
        await asyncio.sleep(random.randint(25, 50))  # Ожидание между кошельками

if __name__ == '__main__':
    asyncio.run(main())
