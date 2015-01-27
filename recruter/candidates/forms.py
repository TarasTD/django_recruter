from django import forms
from django.forms import ModelForm
from candidates.models import *


class ProfileForm(ModelForm):
	class Meta:
		model = Candidate
		fields = ['name', 'surname', 'city', 'current_company', 
				  'email', 'comment', 'specification']