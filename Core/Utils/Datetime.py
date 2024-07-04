import logging
from datetime import datetime, timedelta


class DateTimeHelper:
	def __init__(self, date_str=None):
		self.date_str = date_str  # Строковое представление даты
		self.date_obj = self.get_date_from_string()  # Объект datetime

	def get_date_from_string(self):
		if not self.date_str:
			return None

		try:
			day, month, year = map(int, self.date_str.split('.'))
			if year < 100:  # Если год представлен двумя цифрами
				year += 2000
		except Exception as _error:
			logging.error(f"Ошибка при разборе даты из строки: {_error}")
			return None

		return datetime(year, month, day)

	@staticmethod
	def get_min_date_in_day(date_obj):
		if date_obj:
			return datetime.combine(date_obj.date(), datetime.min.time())
		return None

	def get_min_date_in_obj(self):
		if self.date_obj:
			return datetime.combine(self.date_obj.date(), datetime.min.time())
		return None

	def get_max_date_in_obj(self):
		if self.date_obj:
			return datetime.combine(self.date_obj.date(), datetime.max.time())
		return None

	@staticmethod
	def get_max_date_in_day(date_obj):
		if date_obj:
			return datetime.combine(date_obj.date(), datetime.max.time())
		return None

	def get_min_date_in_day_from_string(self):
		return self.get_min_date_in_day(self.date_obj)

	def get_max_date_in_day_from_string(self):
		return self.get_max_date_in_day(self.date_obj)

	@staticmethod
	def daterange(start_date, end_date):
		for n in range(int((end_date - start_date).days) + 1):
			yield start_date + timedelta(n)
