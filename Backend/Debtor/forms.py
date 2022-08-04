from django import forms
from .models import Contend, Help, Debtor, Post

class ContendForm(forms.ModelForm):

    class Meta:
        model = Contend
        fields = "__all__"

class HelpForm(forms.ModelForm):

    class Meta:
        model = Help
        fields = "__all__"

class DebtorForm(forms.ModelForm):

    class Meta:
        model = Debtor
        fields = "__all__"

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"