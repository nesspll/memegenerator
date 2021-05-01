from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from typing import List
from docx import Document



class DocxIngestor(IngestorInterface):
	"""A class that processes the doc/docx files """
	extension_allowed = ['doc', 'docx']


	@classmethod
	def parse(cls, path: str) -> List[QuoteModel]:
		"""
		A method that parses the doc/docx file and returns a list of Quote objects
		:param path: The Path of doc/docx file.
		:return: List of Quote objects.
		"""
		if not cls.can_ingest(path):
			raise Exception("Cannot ingest with this file extension.")

		quotes = []
		doc_data = Document(path)

		for line in doc_data.paragraphs:
				if line.text != "" or None:
					text_line = line.text.split('-')
					quote = QuoteModel(text_line[0], text_line[1])
					quotes.append(quote)

		return quotes
