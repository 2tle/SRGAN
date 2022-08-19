from tensorflow.python.keras.models import load_model

model_path = 'models/SRGAN_EP100.h5'
change_image_path = ''
model = load_model(model_path)
img = model.predict(change_image_path)





