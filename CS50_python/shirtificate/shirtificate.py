from fpdf import FPDF

class Shirt:
    def __init__ (self, name):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("Helvetica", size=35)
        self.pdf.set_page_background((252,212,255))
        self.pdf.cell(w=0, h=40, txt="CS50 Shirtificate", align="C", new_y="NEXT", new_x="LMARGIN")
        self.pdf.image("shirtificate.png", w=self.pdf.epw, y=90)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.set_font("Helvetica", size=28)
        self.pdf.cell(w=0, h=220, txt=f"{name} took CS50", align="C")
        self.pdf.output("shirtificate.pdf")

name = input("Name: ")
Shirt(name)
