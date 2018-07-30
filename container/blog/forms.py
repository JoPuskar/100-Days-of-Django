from django import forms


class BlogForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your title here...'
    }))
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your body here...'
    }))
    photo = forms.ImageField()
