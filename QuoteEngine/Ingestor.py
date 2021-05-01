from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .csvIngestor import CsvIngestor
from .docxIngestor import DocxIngestor
from .pdfIngestor import PdfIngestor
from .txtIngestor import TxtIngestor


class Ingestor(IngestorInterface):
    """
    A class the selects the appropriate Ingestor for the file provided/or being ingested.
    """
    ingestors = [DocxIngestor, CsvIngestor, TxtIngestor, PdfIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
