from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'surname', 'group', 'email', 'password1', 'password2', ]


#  Лекции
class TrpoLecturesForm(forms.ModelForm):
    """Форма создания новой трпо лекции"""

    class Meta:
        model = TrpoLectures
        fields = '__all__'
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'})
        }


class Pp0201LecturesForm(forms.ModelForm):
    """Форма создания новой пп0201 лекции"""

    class Meta:
        model = PP0201Lectures
        fields = '__all__'
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'})
        }


class Pp0102LecturesForm(forms.ModelForm):
    """Форма создания новой пп0102 лекции"""

    class Meta:
        model = PP0102Lectures
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


#  Практики
class TrpoPracticesForm(forms.ModelForm):
    """Форма создания новой трпо практики"""

    class Meta:
        model = TrpoPractices
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class Pp0201PracticesForm(forms.ModelForm):
    """Форма создания новой пп0201 практики"""

    class Meta:
        model = PP0201Practices
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class Pp0102PracticesForm(forms.ModelForm):
    """Форма создания новой пп0102 практики"""

    class Meta:
        model = PP0102Practices
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


# Оценки
class CreateMarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = '__all__'
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['users_code'].queryset = UserProfile.objects.none()

        print(self.data.get('group'))

        if 'group' in self.data:
            try:
                group = int(self.data.get('group'))
                self.fields['users_code'].queryset = UserProfile.objects.filter(group__id=group).order_by('group__id')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['users_code'].queryset = self.instance.group.userscode_set.order_by('group__id')
