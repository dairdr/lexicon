# -*- encoding: utf-8 -*-
"""Defines all UI forms."""
from django import forms
from django.core.mail import mail_managers

class ContactForm(forms.Form):
	"""Defines the Contact Form."""
	name = forms.CharField()
	sender = forms.EmailField(required=False)
	message = forms.CharField(widget=forms.Textarea())

	def send_form(self, subject='no-subject'):
		"""Sends a email to project managers.

		Keyword arguments:
		subject -- subject of email (default no-subject)

		"""
		name = self.cleaned_data.get('name', 'no-name')
		message = self.cleaned_data.get('message', 'no-message')
		sender = self.cleaned_data.get('sender', 'no-email')
		try:
			mail_managers(subject, message)
		except:
			pass