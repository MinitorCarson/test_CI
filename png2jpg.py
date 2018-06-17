from PIL import Image

def change2jpg(pic_name):
	img = Image.open(pic_name+'.png')
	img =  img.convert('RGB')
	img.save(pic_name+'.jpg')
	print('Finish change2jpg')

