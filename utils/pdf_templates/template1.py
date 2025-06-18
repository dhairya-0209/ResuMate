# utils/pdf_templates/template1.py

from fpdf import FPDF

class Template1(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Resume', ln=True, align='C')
        self.ln(5)

    def section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(0, 0, 128)
        self.cell(0, 10, title, ln=True, align='L')
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def section_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 8, body)
        self.ln(3)
