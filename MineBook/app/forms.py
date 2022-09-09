
from django import forms
from pkg_resources import require
# from .models import Member
from django.core import validators
from django.contrib.auth.models import User

class MemberForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=100)
    user_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    passwd = forms.CharField(max_length=100)
    # img_skin = forms.ImageField(default="",max_length=100)
    class Meta:
        model = User
        fields = ['first_name','last_name','user_name','email','passwd']


# name=forms.CharField()
# email=forms.EmailField()   
# verify_email=forms.EmailField(label='enter your email again') 
# text=forms.CharField(widget=forms.Textarea)
# def clean(self):
#     try: 
#         all_clean_data=super().clean()
#         print(all_clean_data)
#         email=all_clean_data['email']
#         vmail=all_clean_data['verify_email']
#         print(email,vmail)
#         if email!=vmail:
#             raise(forms.ValidationError("make sure emails match!"))
#     except:
#         raise(forms.ValidationError("make sure emails match!"))