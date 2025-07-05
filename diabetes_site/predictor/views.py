from django.shortcuts import render
from .forms import DiabetesForm
import numpy as np
import os
import pickle

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'model/model.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)

def predict_view(request):
    result = None
    if request.method == 'POST':
        form = DiabetesForm(request.POST)
        if form.is_valid():
            data = np.array([[
                form.cleaned_data['pregnancies'],
                form.cleaned_data['glucose'],
                form.cleaned_data['blood_pressure'],
                form.cleaned_data['skin_thickness'],
                form.cleaned_data['insulin'],
                form.cleaned_data['bmi'],
                form.cleaned_data['dpf'],
                form.cleaned_data['age']
            ]])
            prediction = model.predict(data)[0]
            result = "Diabetic" if prediction == 1 else "Not Diabetic"
    else:
        form = DiabetesForm()
    return render(request, 'predictor/predict.html', {'form': form, 'result': result})
