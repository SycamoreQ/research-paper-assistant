# retrieve papers in pdf format and then pre process them into their respective schemas 

from dataset.schema import paper_schema
from dataset.main_arxiv import main_arxiv

PAPER_REPO = '/Users/kaushikmuthukumar/Documents/projects/arxiv_crawler'

class PDFProc : 

    def read_paper(query_word: str  , query_mode: str):
        arxiv_download = main_arxiv(query_word = query_word , query_mode = query_mode)
        
        arxiv_download.run_get_pdf()
    



