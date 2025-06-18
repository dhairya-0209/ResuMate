# utils/pdf_generator.py

import os
from utils.pdf_templates.template1 import Template1
from utils.pdf_templates.template2 import Template2

def generate_pdf(
    name, contact, email, job_title,
    experience, skills, education,
    certifications, languages,
    template_choice=1
):
    # Select template
    if template_choice == 1:
        pdf = Template1()
    else:
        pdf = Template2()

    pdf.add_page()

    # Title - Name & Role
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, name, ln=True, align='C')
    pdf.set_font('Arial', 'I', 12)
    pdf.cell(0, 10, job_title, ln=True, align='C')
    pdf.ln(5)

    # Contact Info
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 8, f"Phone: {contact} | Email: {email}", ln=True, align='C')
    pdf.ln(8)

    # Profile
    pdf.section_title("Profile")
    pdf.section_body(experience)

    # Areas of Expertise
    pdf.section_title("Areas of Expertise")
    skills_text = ', '.join(skills)
    pdf.section_body(skills_text)

    # Education
    pdf.section_title("Education")
    pdf.section_body(education)

    # Certifications
    pdf.section_title("Certifications")
    pdf.section_body(certifications)

    # Languages
    pdf.section_title("Languages")
    pdf.section_body(languages)

    # Save PDF
    output_dir = "outputs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, f"{name}_Resume.pdf")
    pdf.output(output_path)

    return output_path
