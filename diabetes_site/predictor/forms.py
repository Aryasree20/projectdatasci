from django import forms

class DiabetesForm(forms.Form):
    pregnancies = forms.FloatField()
    glucose = forms.FloatField()
    blood_pressure = forms.FloatField()
    skin_thickness = forms.FloatField()
    insulin = forms.FloatField()
    bmi = forms.FloatField()
    dpf = forms.FloatField(label="Diabetes Pedigree Function")
    age = forms.FloatField()