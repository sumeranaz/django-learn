from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.db import models
from django import forms
# Create your models here.

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField(label='E-Mail')
	catagory = forms.ChoiceField(choices=[('question', 'Questions'),('other', 'other')])
	subject = forms.CharField(required=False)
	body = forms.CharField(widget=forms.Textarea)


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.helper = FormHelper
		self.helper.form_method = 'post'

		
class Snippet(models.Model):
	name = models.CharField(max_length=100)
	body = models.TextField()

	def __str__(self):
		return self.name


class SnippetForm(forms.ModelForm):

	class Meta:
		model = Snippet
		fields = ('name', 'body')


