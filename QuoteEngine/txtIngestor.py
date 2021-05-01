from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface



class TxtIngestor(IngestorInterface):
	"""A class that processes the TXT files """
	extension_allowed = ['txt']

	@classmethod
	def parse(cls, path: str) -> List[QuoteModel]:
		"""
		A method that parses the csv file and returns a list of Quote objects
		:param path: The Path of TXT file.
		:return: List of Quote objects.
		"""

		if not cls.can_ingest(path):
			raise Exception("Cannot ingest with this file extension.")

		quotes = []
		with open(path, "r") as txt_file:
			lines = txt_file.readlines()

		for row in lines:
			body, author = row.split('-')
			quotes.append(QuoteModel(body.strip(), author.strip()))

		return quotes

