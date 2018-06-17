from PIL import Image
import png2jpg

def resize_400(pic_name):
	img = Image.open(pic_name+".jpg")
	ResizedImg = img.resize((400,400))
	ResizedImg.save(pic_name+".jpg")

def pre_process(pic_name):
	png2jpg.change2jpg(pic_name)
	resize_400(pic_name)

#pre_process('img_result2')
