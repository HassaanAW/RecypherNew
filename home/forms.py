from django.forms import ModelForm
from django.forms.widgets import Textarea
from .models import User_Emails
from django.forms import ModelForm

class EmailText(ModelForm):
    class Meta:
        model = User_Emails
        fields = ('Body',)
        labels = {
            "Body": ""
        }
