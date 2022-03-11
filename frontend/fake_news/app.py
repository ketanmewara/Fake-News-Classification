# Importing essential libraries
from django.shortcuts import render
from keras.models import load_model
import h5py
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences
# import tensorflow as tf


MODEL = load_model(r'D:\Data Science, AI & ML\Data Science Projects\Machine Learning Projects\Fake News Classifier Using RNN\my_model.h5')

def predict(request):
  #Get the text
  message = request.POST.get('message', 'default')
  print(message)
  datalst = [message]
  voc_size = 5000
  onehot_repr=[one_hot(words,voc_size)for words in datalst] 
  print(onehot_repr)
  sent_length=20
  embedded_docs = pad_sequences(onehot_repr,padding='pre',maxlen=sent_length)
  print(onehot_repr)
  my_prediction = (MODEL.predict(embedded_docs)>0.5).astype("int32")
  print(my_prediction[0])

  #Check whether a news is posstive or not...
  if my_prediction == 1:
    params = {'analyzed_text': 'This is posstive news'}
  else:
    params = {'analyzed_text': 'This is negative news'}

  return render(request, 'result2.html', params)