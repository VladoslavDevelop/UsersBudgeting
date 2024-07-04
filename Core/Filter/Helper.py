from django.db.models import Q


class FilterHelper:
	conditions = {
		'=': '',
		'!=': '!=',
		'>': '__gt',
		'>=': '__gte',
		'<': '__lt',
		'<=': '__lte',
		'in': '__in',
		'not_in': '__in', # В Django нет __not_in, реверсируется __in
		'~': '__contains',
		'i~': '__icontains',
		'between': 'between',
	}

	def __init__(self, queryset, filters):
		self.filters = filters
		self.queryset = queryset

	def apply_filters(self):
		final_filter = Q()

		for field, condition in self.filters.items():
			if field == "or_group":
				or_filter = Q()
				for group_conditions in condition:
					group_filter = Q()
					for or_field, (or_condition_operator, or_value) in group_conditions.items():
						or_django_operator = self.conditions[or_condition_operator]
						if or_django_operator == '!=':
							group_filter &= ~Q(**{f"{or_field}": or_value})
						elif or_condition_operator == 'not_in':
							group_filter &= ~Q(**{f"{or_field}{or_django_operator}": or_value})
						else:
							group_filter &= Q(**{f"{or_field}{or_django_operator}": or_value})
					or_filter |= group_filter
				final_filter &= or_filter
			else:
				if condition is not None:
					if condition[0] == 'between':
						value1, value2 = condition[1]
						final_filter &= Q(**{f"{field}__gte": value1}) & Q(**{f"{field}__lte": value2})
					else:
						condition_operator, value = condition
						django_operator = self.conditions[condition_operator]
						if django_operator == '!=':
							final_filter &= ~Q(**{f"{field}": value})
						elif condition_operator == 'not_in':
							final_filter &= ~Q(**{f"{field}{django_operator}": value})
						else:
							final_filter &= Q(**{f"{field}{django_operator}": value})

		self.queryset = self.queryset.filter(final_filter)
		return self.queryset
