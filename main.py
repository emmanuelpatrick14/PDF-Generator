from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')
# create data frame
pdf = FPDF(orientation='P', unit='mm', format='A4')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align='L', ln=1)
    pdf.line(10, 21, 200, 21)
#
# pdf.add_page()
# #  ADD A PAGE,
# pdf.set_font(family='Times', style='B', size=12)
# # to add text gets 5 args
# pdf.cell(w=0, h=12, txt='hello there!', align='L', ln=1, border=1)
# # ln = break line

pdf.output('output.pdf')