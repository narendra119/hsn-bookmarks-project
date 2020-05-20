from django import forms
from django.contrib.auth import (
  authenticate,
  get_user_model,

  )
from .models import Customer, BookMark
User = get_user_model()

class CreateBookMarkForm(forms.ModelForm):
  class Meta:
    model = BookMark
    fields = "__all__"

class CustomerLoginForm(forms.Form):
  username = forms.CharField(max_length = 200)
  password = forms.CharField(widget= forms.PasswordInput)

  def clean(self, *args, **kwargs):
    """ Clean method is called everytime the form is submitted. """
    username = self.cleaned_data.get('username')
    password = self.cleaned_data.get('password')

    if username and password:
      user = authenticate(username = username, password = password)
      if not user:
        raise forms.ValidationError('')
      if not user.check_password(password):
        raise forms.ValidationError('Wrong Password entered')
      if not user.is_active:
        raise forms.ValidationError('User is not active')
      return super(CustomerLoginForm, self).clean(*args, **kwargs)

class CustomerRegistrationForm(forms.ModelForm):
  email = forms.EmailField(label = 'Enter email address')
  email2 = forms.EmailField(label = 'Confirm email address')
  password = forms.CharField(widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = [
      'username',
      'email',
      'email2',
      'password',
    ]

  def clean(self, *args,**kwargs):
    email = self.cleaned_data.get('email')
    email2 = self.cleaned_data.get('email2')
    if email != email2:
      raise forms.ValidationError("Emails should match")
    email_qs = User.objects.filter(email = email)
    if email_qs.exists():
      raise forms.ValidationError('Email has already been used')
    return super(CustomerRegistrationForm,self).clean(*args, **kwargs)
