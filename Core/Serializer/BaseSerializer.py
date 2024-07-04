import logging

from _decimal import Decimal


class BaseSerializer:
	fields = []
	def __init__(self, entity):
		self.entity = entity

	def serialize(self):
		result = {}
		for field in self.fields:
			value = getattr(self.entity, field, None)
			if callable(value):
				value = value()

			# Получить тип поля
			field_type = self.entity.field_types.get(field)

			# Преобразовать значение в соответствующий тип
			if field_type == str:
				value = str(value)
			elif field_type == int:
				value = int(value)
			elif field_type == bool:
				value = bool(value)
			elif field_type == float:
				value = float(value)
			elif field_type == 'float':
				value = float(value)
			elif field_type == 'date':
				value = value.strftime('%Y-%m-%d') if value else None
			elif field_type == 'datetime':
				value = str(value) if value else None
			elif field_type == 'time':
				value = value.strftime('%H:%M:%S') if value else None
			# Добавьте другие преобразования по необходимости
			if isinstance(value, Decimal):
				value = float(value)

			result[field] = value
		return result
