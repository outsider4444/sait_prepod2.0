import django_filters
from django.forms import DateInput

from .models import *


class MarksFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(
        field_name="date", lookup_expr='gte', widget=DateInput(attrs={'type': 'date'})
    )
    end_date = django_filters.DateFilter(
        field_name="date", lookup_expr='lte', widget=DateInput(attrs={'type': 'date'})
    )
    group = django_filters.ChoiceFilter(choices=FILTER_CHOICES)

    class Meta:
        model = Marks
        fields = '__all__'
        exclude = ['date', 'items_code', 'group', 'users_code', 'mark', 'comment']


class UserMarksFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(
        field_name="date", lookup_expr='gte', widget=DateInput(attrs={'type': 'date'})
    )
    end_date = django_filters.DateFilter(
        field_name="date", lookup_expr='lte', widget=DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Marks
        fields = '__all__'
        exclude = ['date', 'items_code', 'group', 'users_code', 'mark', 'comment']