from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from .models import User
from django.utils.translation import gettext_lazy as _

# class StudentRegisterForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', 'gender', 'contact_number')

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_student = True
#         user.save()
#         return user

# GENDER_CHOICES = (
#     ('M', 'Male'),
#     ('F', 'Female'),
#     ('O', 'Other'),
# )

# class StudentRegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True, help_text=_('Required. Enter a valid email address.'))
#     gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, required=True)
#     contact_number = forms.CharField(required=True, max_length=15, help_text=_('Required. Enter a valid contact number.'))

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', 'gender', 'contact_number')

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_student = True
#         user.save()
#         return user

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
#         self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
#         self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
#         self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})
#         self.fields['gender'].widget.attrs.update({'class': 'form-check-input'})
#         self.fields['contact_number'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contact Number'})


class StudentRegisterForm(UserCreationForm):
    email = forms.EmailField()

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    # gender = forms.ChoiceField(choices=GENDER_CHOICES)
    gender = forms.CharField(max_length=10, widget=forms.Select(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')]))

    contact_number = forms.CharField(max_length=15)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2','gender', 'contact_number')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        return user

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if gender == 'M':
            return True
        elif gender == 'F':
            return False
        else:
            raise ValidationError("Invalid gender value")