import PyPDF2
import tabula
from tkinter.filedialog import askopenfilename



# df = tabula.read_pdf("Y:\dwg\משרד שיכון\מחירון\documents_tichnun_ironi_infrastructure_and_paving_price_list.pdf", pages='all')

tabula.convert_into("Y:\dwg\משרד שיכון\מחירון\documents_tichnun_ironi_infrastructure_and_paving_price_list.pdf", "output.csv", output_format="csv", pages'=['7:]')