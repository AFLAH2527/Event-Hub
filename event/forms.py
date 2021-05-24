from django.forms import ModelForm
from .models import Join

class JoinForm(ModelForm):
    class Meta:
        model = Join
        fields = '__all__'
    