

class QuoteModel:
	"""Class object model that models a quote."""
	def __init__(self, body: str, author: str):
		"""
		Initialization of the QuoteModel object
		:param body:
		:param author:
		"""
		self.body = body
		self.author = author

	def __str__(self):
		"""Object representation in string format - Human-Readable"""
		return f'{self.body} - quote of {self.author}'

	def __repr__(self):
		"""Object representation in string format - Object Official"""
		return f'{self.body} - {self.author}'