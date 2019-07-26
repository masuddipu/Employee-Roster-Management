from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

from .models import User

class SignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=50)
    location = forms.CharField(max_length=264)
    profile_pic = forms.ImageField()
    class Meta(UserCreationForm.Meta):
        model = User

    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_emp = True
    #     user.save()
    #
    #     profile = UserProfile.objects.create(user=user)
    #     profile.phone = self.cleaned_data.get('phone')
    #     profile.location = self.cleaned_data.get('location')
    #     profile.profile_pic = self.cleaned_data.get('profile_pic')
    #     profile.save()
