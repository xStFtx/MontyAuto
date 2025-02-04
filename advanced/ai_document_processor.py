import os
from transformers import pipeline
import PyPDF2

class DocumentAI:
    def __init__(self):
        self.ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    def process_pdf(self, file_path):
        text = self._extract_text(file_path)
        entities = self.ner(text)
        summary = self.summarizer(text, max_length=130, min_length=30, do_sample=False)
        return {
            "entities": entities,
            "summary": summary[0]['summary_text'],
            "metadata": self._extract_metadata(file_path)
        }

    def _extract_text(self, path):
        with open(path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            return '\n'.join([page.extract_text() for page in reader.pages])

    def _extract_metadata(self, path):
        return {
            "file_name": os.path.basename(path),
            "file_size": os.path.getsize(path),
            "pages": len(PyPDF2.PdfReader(path).pages)
        } 