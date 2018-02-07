from django.forms import ModelForm

from .models import User


# https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
