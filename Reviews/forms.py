from django import forms
from Reviews.models import *



class UserForm(forms.ModelForm):
    class Meta():
        model=User
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput}



class QuestionForm(forms.ModelForm):
    class Meta():
        model=Question
        fields=['question']
        widgets={'question':forms.Textarea(attrs={'cols':50, 'rows':4})}



class AnswerForm(forms.ModelForm):
    class Meta():
        model=Answer
        fields=['question','answer']
        widgets={'answer':forms.Textarea(attrs={'cols':50, 'rows':5})}
