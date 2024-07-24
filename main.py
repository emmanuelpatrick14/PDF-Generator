from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')
# create data frame
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)


for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align='L', ln=1)
    pdf.line(10, 21, 200, 21)

    #     add a break line to set footer
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    #
    # range method give a list of the holder number of items specified in the call
    for i in range(row['Pages'] - 1):
        pdf.add_page()
        # add a break line to set footer
        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

# pdf.add_page()
# #  ADD A PAGE,
# pdf.set_font(family='Times', style='B', size=12)
# # to add text gets 5 args
# pdf.cell(w=0, h=12, txt='hello there!', align='L', ln=1, border=1)
# # ln = break line

pdf.output('output.pdf')
