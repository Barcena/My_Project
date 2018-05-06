import joblib
# load the model from disk
def predict_model(instance, new_result=None):
	loaded_model = joblib.load('static/sav/model.sav')
	result = loaded_model.predict([[instance.amount, instance.inflation]])
	return result
