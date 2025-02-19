from aiohttp_proxy import ProxyConnector
import aiohttp
import sys
import asyncio

async def async_get(
		url: str,
		proxy: str | None = None,
		headers: dict | None = None,
		response_type: str = 'json',
		**kwargs
) -> dict | str | None:

	if proxy and 'http://' not in proxy:
		proxy = f'http://{proxy}'

	connector = ProxyConnector.from_url(
		url=proxy
	) if proxy else None

	async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
		async with session.get(url=url, **kwargs) as response:
			status_code = response.status
			if response_type == "json":
				response = await response.json()
			elif response_type == "text":
				response = await response.text()
			if status_code <= 201:
				return response

			raise Exception(response)

async def check_ip(proxy: str):
	for i in range(3):
		try:
			r = await async_get(url='http://eth0.me/', proxy=proxy, response_type='text')
			if r.strip() not in proxy:
				await asyncio.sleep(1)
			else:
				# print(f'Proxy {proxy} is good')
				return True
		except Exception as e:
			await asyncio.sleep(1)
	print(f'Proxy: {proxy} does not work')
	return False

def open_proxies(path: str, addresses_count: int):
	print(f'Subscribe to https://t.me/degen_statistics 🤫')
	try:
		with open(path, 'r') as file:
			proxies = [line.strip() for line in file if line.strip()]
	except FileNotFoundError:
		print(f"Error: File '{path}' not found.")
		return None
	except Exception as e:
		print(f"An error occurred while reading the file: {e}")
		return None

	if not proxies:
		print('No proxies provided. Will use your IP.')
		return None

	if len(proxies) != addresses_count:
		print(f"Error: Expected {addresses_count} proxies, but found {len(proxies)} in '{path}'.")
		sys.exit(1)
	print('Number of proxies matches the required addresses. Will use proxies.')
	return proxies

async def change_ip(CHANGE_IP_LINK):
	for i in range(3):
		try:
			change = await async_get(url=CHANGE_IP_LINK)
			if change.get('status') == 'OK':
				return True
		except Exception as e:
			print(f"An error occurred while changing the IP: {e}")
			await asyncio.sleep(1)