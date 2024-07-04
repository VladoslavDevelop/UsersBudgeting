class BaseEntity:
	def __init__(self, model_instance):
		self.model_instance = model_instance
		self.field_types = self.get_field_types_from_model()
		self.prepare_fields()

	def get_field_types_from_model(self):
		field_types = {}
		for field in self.model_instance._meta.fields:
			field_name = field.name
			internal_type = field.get_internal_type()

			if internal_type in ['CharField', 'TextField', 'SlugField', 'EmailField', 'URLField']:
				field_type = str
			elif internal_type in ['IntegerField', 'BigIntegerField', 'SmallIntegerField', 'PositiveIntegerField']:
				field_type = int
			elif internal_type in ['BooleanField']:
				field_type = bool
			elif internal_type in ['FloatField', 'DecimalField']:
				field_type = float
			elif internal_type in ['DateField']:
				field_type = 'date'
			elif internal_type in ['DateTimeField']:
				field_type = 'datetime'
			elif internal_type in ['TimeField']:
				field_type = 'time'
			elif internal_type in ['FileField']:
				field_type = 'file'
			elif internal_type in ['ImageField']:
				field_type = 'image'
			elif internal_type in ['UUIDField']:
				field_type = 'uuid'
			else:
				continue
			field_types[field_name] = field_type
		return field_types

	def prepare_fields(self):
		for field_name, field_type in self.field_types.items():
			value = getattr(self.model_instance, field_name)
			if callable(value):
				value = value()  # Вызов функции, если значение является функцией
			setattr(self, field_name, value)

	def to_representation(self):
		representation = {}
		for field_name, field_type in self.field_types.items():
			representation[field_name] = getattr(self, field_name)
		return representation
