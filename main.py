import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")


for filepath in filepaths:

    pdf = FPDF(orientation="P", unit='mm', format='A4')
    pdf.add_page()


    filename = Path(filepath).stem
    invoice_no, date = filename.split("-")

    pdf.output(f"PDFs/{filename}.pdf")