from django import forms
from .models import Teacher
#from . import views

class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'
