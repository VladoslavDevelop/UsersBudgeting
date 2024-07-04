from django.core.exceptions import ValidationError


class BaseField:
	def __init__(self, required=True, read_only=None, write_only=None):
		self.read_only = read_only
		self.write_only = write_only
		self.required = required

	def to_representation(self, value):
		if self.write_only:
			pass
		else:
			return value

	def to_internal_value(self, data):
		return data

	def validate(self, value):
		if self.required and value is None:
			raise ValidationError('This field is required.')
		return value


class CharField(BaseField):
	def __init__(self, **kwargs):
		self.max_length = kwargs.pop('max_length', None)
		self.min_length = kwargs.pop('min_length', None)
		super().__init__(**kwargs)

	def validate(self, value):
		value = super().validate(value)
		if self.max_length is not None:
			if len(value) > self.max_length:
				raise ValidationError('Max Length')
		if self.min_length is not None:
			if len(value) < self.min_length:
				raise ValidationError('Min Length')
		return str(value).strip()


class FloatField(BaseField):
	def __init__(self, **kwargs):
		self.max_length = kwargs.pop('max_length', None)
		self.min_length = kwargs.pop('min_length', None)
		super().__init__(**kwargs)

	def validate(self, value):
		value = super().validate(value)
		if self.max_length is not None:
			if len(value) > self.max_length:
				raise ValidationError('Max Length')
		if self.min_length is not None:
			if len(value) < self.min_length:
				raise ValidationError('Min Length')
		return str(value).strip()

	def to_representation(self, value):
		return float(value)
