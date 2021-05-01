from typing import List

import os
import subprocess
import random

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface



class PdfIngestor(IngestorInterface):
	"""A class that processes the PDF files """
	extension_allowed = ['pdf']


	@classmethod
	def parse(cls, path: str) -> List[QuoteModel]:
		"""
		A method that parses the csv file and returns a list of Quote objects
		:param path: The Path of PDF file.
		:return: List of Quote objects.
		"""

		if not cls.can_ingest(path):
			raise Exception("Cannot ingest with this file extension.")

		temp = f"./tmp/{str(random.randint(0, 1000))}.txt" # temporary location for processing/generating text files
		quotes = []

		try:
			"""This variable initiates the conversion from PDF to TEXT."""
			init_conversion = subprocess.run(["pdftotext", "-layout", path, temp], timeout=2)
			with open(temp, 'r') as txt_files:
				text_lines = txt_files.readlines()
		except FileNotFoundError:
			print('pdftotext is not available.')
			return quotes


		for line in text_lines:
			line = line.strip('\n\r').strip()
			if len(line) > 0:
				parse_line = line.split(' - ')
				quote = QuoteModel(body=parse_line[0], author=parse_line[1])
				quotes.append(quote)

		subprocess.run["rm", temp]

		return quotes

