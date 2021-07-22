import PyPDF2
import tabula
from tkinter.filedialog import askopenfilename



# df = tabula.read_pdf("Y:\dwg\משרד שיכון\מחירון\documents_tichnun_ironi_infrastructure_and_paving_price_list.pdf", pages='all')
filename = askopenfilename()
tabula.convert_into(filename, filename +'.csv", output_format="csv", pages=[74,75,76])
print('Finished')