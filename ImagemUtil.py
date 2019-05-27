import PIL

BASE_WIDTH = 180
BASE_HEIGHT = 0

class ImagemUtil:
	WIDTH = 40
	HEIGHT = 90

	@classmethod
	def ajustaImagem(self,image):
		wpercent = (BASE_WIDTH / float(image.size[0]))
		BASE_HEIGHT = int((float(image.size[1]) * float(wpercent)))
		image = image.resize((BASE_WIDTH, BASE_HEIGHT), PIL.Image.ANTIALIAS)
		return image


