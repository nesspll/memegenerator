from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from typing import List

import pandas as pd


class CsvIngestor(IngestorInterface):
	"""A class that processes the CSV files """
	extension_allowed = ['csv']

	@classmethod
	def parse(cls, path: str) -> List[QuoteModel]:
		"""
		A method that parses the csv file and returns a list of Quote objects
		:param path: The Path of CSV file.
		:return: List of Quote objects.
		"""

		if not cls.can_ingest(path):
			raise Exception("Cannot ingest with this file extension.")

		quotes = []
		csv_data = pd.read_csv(path, header=0, delimiter=',')

		for _, row in csv_data.iterrows():
			quote = QuoteModel(body=row['body'], author=row['author'])
			quotes.append(quote)

		return quotes

