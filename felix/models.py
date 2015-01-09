from django import forms

class ContactForm(forms.Form):

    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
	# sender_name = forms.CharField(label="name", max_length=100)
	# email = forms.EmailField(label="email")
	# message = forms.CharField(label="message", widget=forms.Textarea)
