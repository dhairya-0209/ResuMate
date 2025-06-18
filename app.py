# app.py

from skills_data import job_skills
from utils.resume_builder import build_resume
from utils.pdf_generator import generate_pdf

def main():
    # Inputs
    name = input("Enter your name: ")
    contact = input("Enter your contact info: ")
    qualification = input("Enter your qualification: ")
    job_title = input("Enter job title: ")

    # Skills auto-fill
    skills = job_skills.get(job_title, ["Communication", "Teamwork", "Adaptability"])

    # Build resume text
    resume_text = build_resume(
        template_path="templates/resume_template.txt",
        name=name,
        contact=contact,
        qualification=qualification,
        job_title=job_title,
        skills=skills
    )

    # Generate PDF
    generate_pdf(
        resume_text,
        output_path="outputs",
        filename=f"{name.replace(' ', '_')}_resume.pdf"
    )

    print("🎯 Resume successfully generated and saved in 'outputs/' folder!")

if __name__ == "__main__":
    main()

