from users.models import BlacklistedToken


class BaseController:
	serializer_data: dict or list = None
	error_data: dict = None
	post_data: dict = None
	_required_parameters: list = []
	_default_message: dict = None
	user = None
	locale: str = 'ru'
	token = None

	def validate_parameters(self, request):
		locale = request.GET.get('locale', 'ru')
		self.locale = locale
		self.user = request.user
		errors = {}
		for param in self._required_parameters:
			if request.method == 'GET':
				value = request.GET.get(param, None)
			elif request.method == 'POST':
				value = request.data.get(param, None)
			else:
				# TODO Добавить другие типы запросов
				value = None
			if value is None:
				error_message_template = self._default_message.get('errors').get('field_not_provided').get(locale,
																										   'Error')
				error_message = error_message_template.format(field_name=param)
				errors[param] = error_message
		self.error_data = errors

	def check_available_token(self):
		"""
		Метод для проверки доступности токена.
		:return:
		"""

		check_token = BlacklistedToken.objects.filter(token=self.token)
		if check_token.exists():
			self.error_data['token'] = 'Токен пользователя заблокирован'
			return

	def success_response(self):
		result = {
			'status': 'success',
			'result': self.serializer_data
		}
		return result

	def error_response(self):
		result = {
			'status': 'error',
			'result': self.error_data
		}
		return result
