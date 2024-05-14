from django import forms
from customer.models import *

class Menuform(forms.ModelForm):
	name = forms.CharField(max_length=100)
	price = forms.DecimalField(max_digits=5, decimal_places=2)
	category = forms.CharField(max_length=100)
	image = forms.ImageField()

	class Meta:
		model = MenuItem
		fields  = "__all__"
	



'''
category = forms.ModelMultipleChoiceField(
            queryset=Category.objects.all(),
    )
	
	<select name="category id="category" multiple>
                    <option value="Cakes">Cake</option>
                    <option value="Cookies">Cookie</option>

                </select> 
				
				
				category = forms.ModelMultipleChoiceField(
		queryset=Category.objects.all(),
		widget=forms.CheckboxSelectMultiple
    )'''