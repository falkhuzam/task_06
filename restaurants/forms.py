from django import forms
from .models import Restaurant


class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields= "__all__"
	# """docstring for RestaurantForm"""
	# def __init__(self, arg):
	# 	super RestaurantForm, self).__init__()
	# 	self.arg = arg
		