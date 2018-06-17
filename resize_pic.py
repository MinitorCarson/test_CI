from PIL import Image
import png2jpg
import os

def resize_400(pic_name):
	img = Image.open(pic_name+".jpg")
	ResizedImg = img.resize((400,400))
	ResizedImg.save(pic_name+".jpg")

def pre_process(pic_name):
	png2jpg.change2jpg(pic_name)
	resize_400(pic_name)
	isexit=False
	while isexit==False:
		isexit=os.path.exists('/root/web/get.png')
		print('wait')
	#return 1
	print('Finish pre_process')
	return 1

pre_process('get')

