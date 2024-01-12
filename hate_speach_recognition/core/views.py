# # views.py
# from django.http import JsonResponse

# def submit_data(request):
#     if request.method == 'POST':
#         user_input = request.POST.get('user_input')
#         # Process the input or submit it to an endpoint
#         return JsonResponse({'message': 'Data submitted successfully'})
#     return JsonResponse({'error': 'Invalid request'})
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse
# from .models import UserInput
from joblib import load
from scipy.sparse import csr_matrix
import os
from django.conf import settings

# Custom pad_sequences function
def pad_sequences(sequences, maxlen, padding='post', value=0):
    # Creating a new zero-filled matrix
    padded_sequences = np.zeros((len(sequences), maxlen))
    for i, seq in enumerate(sequences):
        if len(seq) > maxlen:
            # Truncate the sequence if it is longer than maxlen
            padded_sequences[i] = np.array(seq[:maxlen])
        else:
            # Pad the sequence with the specified value
            if padding == 'post':
                padded_sequences[i, :len(seq)] = np.array(seq)
            else:  # 'pre' padding
                padded_sequences[i, -len(seq):] = np.array(seq)
    return padded_sequences

# Set the path to the model and tokenizer
model_path = os.path.join(settings.BASE_DIR,'models', 'bert_model.joblib')

model = load(model_path)

def predict_hate_speech(request):
    if request.method == 'POST':
        input_text = request.POST.get('inputText')
       
        prediction = model.predict(input_text)
        
        # #predicted_class = "Hate Speech" if float(prediction[0]) > 0.5 else "Not Hate Speech"
        predicted_class = prediction[0]
       
        return JsonResponse({'prediction'})
    return render(request, 'hate_speech_form.html')