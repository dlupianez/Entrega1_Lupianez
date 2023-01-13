from django import forms

class ApartmentForm(forms.Form):
    door_number=forms.IntegerField()
    rental_value=forms.FloatField()
    garage_value=forms.FloatField()
    expenses_value=forms.FloatField()
    total_value=forms.FloatField()