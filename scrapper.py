import asyncio
from utils import async_get, change_ip

class Scrapper:
	def __init__(self, proxy):
		self.proxy = proxy

	async def balance(self, wallet:str):
		url = f'https://monad-api.blockvision.org/testnet/api/account/tokenPortfolio'
		params = {
			'address': wallet,
		}
		for i in range(5):
			try:
				res = await async_get(url=url, proxy=self.proxy, params=params)
				bal = res['result']['data']
				if len(bal) > 0:
					bal = bal[0]['balance']
				else:
					bal = 0
				return {'wallet': wallet, 'balance':bal}

			except Exception as e:
				print(e)
				await asyncio.sleep(1)


