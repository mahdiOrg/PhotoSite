from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import re


def is_english(string):  # this is just for check username.
    """
    Returns True if the given string contains only English characters
    """
    pattern = r'^[a-zA-Z ]+$'
    return bool(re.match(pattern, string))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': "نام کاربری"}))
    password = forms.CharField(max_length=250, widget=forms.PasswordInput(
        attrs={'style': 'width:100%;height:45px', 'placeholder': "گذرواژه"}))

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data
        else:
            raise ValidationError('اطلاعات وارد شده معتبر نیست')


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': "نام کاربری"}))
    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': "نام"}))
    password = forms.CharField(max_length=250, widget=forms.PasswordInput(
        attrs={'class': 'password_custome', 'placeholder': "گذرواژه"}))
    password_check = forms.CharField(max_length=250, widget=forms.PasswordInput(
        attrs={'class': 'password_custome', 'placeholder': "تکرار گذرواژه"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if not is_english(username):
            raise ValidationError('نام کاربری باید انگلیسی باشد')
        elif User.objects.filter(username=username).exists():
            raise ValidationError('نام کاربری در حال حاضر وجود دارد! نام دیگری انتخاب کنید')
        else:
            return self.cleaned_data.get('username')

    def clean_password_check(self):
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('password_check')
        if pass1 == pass2:
            return self.cleaned_data
        else:
            raise ValidationError('گذرواژه ها مطابقت ندارند')
