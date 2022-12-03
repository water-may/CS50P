#! /usr/bin/python3.10

from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.set_font("Times","B", size=30)
    pdf.add_page()
    pdf.image("shirtificate.png", x=0.1, y=50)
    pdf.text(x=70, y=30,txt='CS50 Shirtificate')
    text = f"{name} took cs50."
    pdf.set_font("Helvetica", size=25)
    pdf.set_text_color(r=255,b=255,g=255)
    pdf.text(x=65, y=130,txt=text)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()