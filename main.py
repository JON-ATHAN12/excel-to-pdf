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

    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice no. {invoice_no}", ln=1)

    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    df = pd.read_excel(filepath, sheet_name='Sheet 1')

    # Add Header
    columns = df.columns
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family="Times", style='B', size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=60, h=8, txt=columns[1], border=1)
    pdf.cell(w=40, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)



    pdf.output(f"PDFs/{filename}.pdf")