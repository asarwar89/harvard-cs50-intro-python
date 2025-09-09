from fpdf import FPDF

class PDF(FPDF):
  def header(self):
    # Rendering logo:
    name = input("Name: ")
    self.image("shirtificate.png", 'center', 70, 150, 150)
    
    # Setting font: helvetica bold 15
    self.set_font("helvetica", style="B", size=50)
    
    # Printing title:
    self.set_x((self.w - 100) / 2)
    self.cell(100, 60, "CS50 Shirtificate", align="C")
    # Performing a line break:
    self.ln(100)
    self.set_font("helvetica", style="B", size=22)
    self.set_text_color(255, 255, 255)
    self.set_x((self.w - 100) / 2)
    self.multi_cell(100, 10, f"{name} took CS50", align="C")


# Instantiation of inherited class
pdf = PDF()
pdf.add_page("Portrait", "A4")
pdf.output("shirtificate.pdf")