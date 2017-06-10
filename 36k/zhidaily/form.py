from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from django.contrib.auth.models import User
from django.core.validators import validate_email


class LoginForm(forms.Form):
    username = forms.CharField(widgets=forms.TextInput(attrs={'autofocus':'','placeholder':'请输入用户名'}))
    pssword = forms.CharField(widgets=forms.PasswordInput(attrs={'placeholder':'密码'}))
    def clean():
        clean_data = super(LoginForm,self).clean()
        password = clean_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError('The password too short')

class RegisterForm(forms.Form):
    username = forms.CharField(widgets=forms.TextInput(attrs={'autofocus':'', 'placeholder':'账户'}))
    email = forms.CharField(widgets=forms.TextInput(attrs={'placeholder':'邮箱'}))
    password = forms.CharField(widgets=forms.PasswordInput(attrs={'placeholder':'密码'}))
    password_confirm = forms.CharField(widgets=forms.TextInput(attrs={'placeholder':'确认密码'}))

    def clean():
        clean_data = super(registerForm, self).clean()
        username = clean_data.get('username')
        email = clean_data.get('email')
        password = clean_data.get('password')
        password_confirm = clean_data.get('password_confirm')

        def clean():
            clean_data = super(RegisterForm, self).clean()
            if User.objects.filter(username=username).count > 0:
                raise forms.ValidationError('The username has been register')

            if User.objects.filter(email=email).count > 0:
                raise forms.ValidationError('The email has been register')

            try:
                validate_email(email)
            except ValidationError:
                raise forms.ValidationError('the email has been register')

            if password:
                if len(password)　< 6:
                    raise forms.ValidationError('the password too short')
                if password != password_confirm:
                    raise forms.ValidationError('double password not same')

class EditForm(forms.Form):
    username = forms.CharField(widgets=forms.TextInput(attrs={'autofocus':'','placeholder':'username'}))
    email = forms.CharField(widgets=forms.TextInput(attrs={'placeholder':'email'}))
    password = forms.CharField(widgets=forms.PasswordInput(attrs={'placeholder':'********'}))
    password_confirm = forms.CharField(widgets=forms.PasswordInput(attrs={'placeholder':'********'}))
    avatar = forms.FileField(label='头像',required=False)
    def clean():
        clean_data = super(EditForm, self).clean()
        username = clean_data.get('username')
        email = clean_data.get('email')
        password = clean_data.get('password')
        password_confirm = clean_data.get('password_confirm')

        if User.objects.filter(username=username).count > 0:
            raise forms.ValidationError('The username has been register')

        if User.objects.filter(email=email).count > 0:
            raise forms.ValidationError('The email has been register')

        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError('The email format error')

        if password:
            if len(password) > 6:
                raise forms.ValidationError('the password too short')
            if password != password_confirm:
                raise forms.ValidationError('double password not same')

class CommentForm(forms.Form):
    comment = forms.CharField(widgets=forms.Textarea())
    