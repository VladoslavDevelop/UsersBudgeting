import requests


class AMLCheck:
	"""
	Класс для проверки транзакций на наличие в списке санкций

	"""
	base_url = "https://aml.cryptocloud.plus/"
	refresh_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5OTQzNjQ3OCwiaWF0IjoxNjk5MzUwMDc4LCJqdGkiOiIzNDgxZmU1OTBiMzQ0OTYxYjcxODAyOGNlYTkxNTkzNyIsInVzZXJfaWQiOjF9.J8yEbUiGVh-toJKJQ48os59OPJaGpWnknEsEzDhtr0M"
	token_auth = None
	sub_id = "c9qezowlQzKKPxHP"

	def authentication(self):
		"""
		Аутентификация
		:return:
		"""

		payload = {
			"refresh": self.refresh_token
		}

		path = f"{self.base_url}auth/jwt/refresh/"

		response = requests.post(path, json=payload)

		if response.status_code == 200:

			self.token_auth = response.json().get('access', None)

			return True

		else:

			return False

	def check(self, inv_id: str, address: str, tx_id: str, currency: str) -> dict:
		"""
		Проверяет транзакцию на наличие в списке санкций
		:param inv_id: id инвойса
		:param address: адрес получателя
		:param tx_id: hash транзакции
		:param currency: валюта
		:return:
		"""

		if self.token_auth is None:
			self.authentication()

		payload = {
			"inv_id": f"{inv_id}",
			"address": f"{address}",
			"tx_id": f"{tx_id}",
			"currency": f"{currency}",
			"sub_id": f"{self.sub_id}"
		}

		path = f"{self.base_url}aml_check/create"

		headers = {
			"Authorization": f"Bearer {self.token_auth}",
			"Content-Type": "application/json"
		}

		response = requests.post(path, json=payload, headers=headers)

		if response.status_code == 200:

			data_json = response.json()

			if data_json.get('status') == 'success':

				return data_json.get('result')

			else:

				return data_json.get('result')

		else:
			return {'error': f'error {response.text}'}
