from django import forms

class ContactForm(forms.Form):
	sender_name = forms.CharField(label="name", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
	email = forms.EmailField(label="email", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	message = forms.CharField(label="message", widget=forms.Textarea(attrs={'placeholder' : 'Message' }))
