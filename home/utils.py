import joblib
from numpy.random import random
# load the model from disk
def predict_model(instance, new_result=None):
	loaded_model = joblib.load('static/sav/model.sav')
	result = loaded_model.predict([[instance.amount, instance.inflation]])
	if result and instance.inflation > 15:
		if random() > 0.4:
			result = 0
	return result
