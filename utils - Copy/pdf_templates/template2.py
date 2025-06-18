# utils/pdf_templates/template2.py

from fpdf import FPDF

class Template2(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 18)
        self.cell(0, 10, 'Resume', ln=True, align='C')
        self.ln(8)

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 13)
        self.set_text_color(50, 50, 150)
        self.cell(0, 8, title, ln=True, align='L')
        self.set_text_color(0, 0, 0)
        self.ln(1)

    def section_body(self, body):
        self.set_font('Helvetica', '', 11)
        self.multi_cell(0, 7, body)
        self.ln(2)
