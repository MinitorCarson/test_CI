from keras.layers import Conv2D, UpSampling2D, InputLayer, Conv2DTranspose
from keras.layers import Activation, Dense, Dropout, Flatten
from keras.layers.normalization import BatchNormalization
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from skimage.color import rgb2lab, lab2rgb, rgb2gray, xyz2lab
from skimage.io import imsave
import numpy as np
import os
import random
import tensorflow as tf
from keras.models import load_model
import os
import resize_pic

os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"
def generate_colorpic(picname,result_name):
	# preprocess picture
	# picname='cai'
	resize_pic.pre_process(picname)

	# Get images
	image = img_to_array(load_img(picname+'.jpg'))
	image = np.array(image, dtype=float)

	X = rgb2lab(1.0/255*image)[:,:,0]
	print (X)
	Y = rgb2lab(1.0/255*image)[:,:,1:]
	Y /= 128
	X = X.reshape(1, 400, 400, 1)
	Y = Y.reshape(1, 400, 400, 2)

	# Building the neural network
	model = Sequential()
	model.add(InputLayer(input_shape=(None, None, 1)))
	model.add(Conv2D(8, (3, 3), activation='relu', padding='same', strides=2))
	model.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
	model.add(Conv2D(16, (3, 3), activation='relu', padding='same'))
	model.add(Conv2D(16, (3, 3), activation='relu', padding='same', strides=2))
	model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
	model.add(Conv2D(32, (3, 3), activation='relu', padding='same', strides=2))
	model.add(UpSampling2D((2, 2)))
	model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
	model.add(UpSampling2D((2, 2)))
	model.add(Conv2D(16, (3, 3), activation='relu', padding='same'))
	model.add(UpSampling2D((2, 2)))
	model.add(Conv2D(2, (3, 3), activation='tanh', padding='same'))

	# Finish model
	model.compile(optimizer='rmsprop', loss='mse')

	# model.fit(x=X, y=Y, batch_size=1, epochs=1000)

	del model  # deletes the existing model  
	model = load_model('my_swim_model2.h5') 

	print(model.evaluate(X, Y, batch_size=1))
	output = model.predict(X)
	output *= 128
	# Output colorizations
	cur = np.zeros((400, 400, 3))
	cur[:,:,0] = X[0][:,:,0]
	cur[:,:,1:] = output[0]
	# cur[:,:,1:] = Y[0][:,:,1:]
	imsave(result_name+".png", lab2rgb(cur))
	#imsave("img_gray_version.png", rgb2gray(lab2rgb(cur)))
	return 	1






generate_colorpic('get','re')
