from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
	"""Abstract Base Class for Ingestor Class"""

	extension_allowed = []  # Extensions allowed to be ingested.

	@classmethod
	def can_ingest(cls, path) -> bool:

		"""
		Checks if the file can be ingested/parsed.

		:param path: Path of the file location
		:return: Return's the extension and true if file is allowed to be ingested.
		"""
		ext = path.split(".")[-1]
		return ext in cls.extension_allowed

	@classmethod
	@abstractmethod
	def parse(cls, path: str) -> List[QuoteModel]:
		"""
		This method parses the file.

		:param path: The path of the file.
		:return:  The List of Quotes.
		"""
		pass
