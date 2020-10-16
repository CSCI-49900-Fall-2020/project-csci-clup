from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerSignUpForm(UserCreationForm):
    # middle_name = forms.CharField(max_length=100, help_text='')
    cell_number = forms.CharField(max_length=12, help_text='')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email',  'cell_number')


class BusinessSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=12, help_text='')
    store_name = forms.CharField(max_length=100, help_text='')
    store_number = forms.CharField(max_length=12, help_text='')
    store_address = forms.CharField(max_length=100, help_text='')
    city = forms.CharField(max_length=30, help_text='')
    state = forms.CharField(max_length=2, help_text='')
    zipcode = forms.CharField(max_length=5, help_text='')
    title_choice = (
        ('Mr.', 'Mr.'),
        ('Ms.', 'Ms.'),
    )
    input_sex = forms.ChoiceField(choices=title_choice)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'store_name', 'store_number', 'password1',
                  'password2', 'store_address', 'city', 'state', 'zipcode', 'input_sex')