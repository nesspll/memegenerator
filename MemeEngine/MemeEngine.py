from PIL import Image, ImageDraw, ImageFont
from uuid import uuid4
from random import randint
import os




class MemeEngine:
	""" A class that creates a meme using quotes."""

	def __init__(self, outputDir):
		"""
		Initialization of parameters.

		:param outputDir: Output location.
		:return: None
		"""
		self.outputDir = outputDir

	def meme(self, imgPath: str, body: str, author: str,
	              imgWidth: int = 500) -> str:
		"""
		This method/function generates a meme based on certain inputs.
		:param imgPath: The path to the image.
		:param body: The text of the quote
		:param author: The author of the quote
		:param imgWidth: The width of the image
		:return: path location of the meme
		"""
		img = Image.open(imgPath)

		imgRatio = imgWidth / float(img.size[0])
		imgHeight = int(imgRatio * float(img.size[1]))

		imagePosition = (randint(0, 150), randint(0, 250))

		img = img.resize((imgWidth, imgHeight), Image.NEAREST)
		font = ImageFont.truetype(os.path.abspath('./_data/fonts/CookieCrisp.ttf'), 17)
		drawImage = ImageDraw.Draw(img)

		drawImage.text(imagePosition, f"{body} - {author}", color=(0, 0, 0), font=font)

		file_name = f"{uuid4()}.png"
		path = os.path.join(self.outputDir, file_name)

		img.save(path)

		return path