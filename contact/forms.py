from django import forms


class MessageForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'ایمیل '}), required=False)
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'پیام خود را بنویسید ...'}))
