from django import forms
from customer.models import *

class Reviewform(forms.ModelForm):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	review = models.TextField()
	class Meta:
		model = ReviewModel
		fields  = "__all__"