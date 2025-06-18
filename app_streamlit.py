import streamlit as st
from utils.resume_builder import build_resume
from utils.pdf_generator import generate_pdf
from skills_data import job_title_skills
from utils.job_role_converter import convert_resume_for_job_role
from utils.ats_checker import check_ats_score
from utils.job_search import search_jobs
from utils.skill_matcher import match_skills
import os
from PyPDF2 import PdfReader
import requests

def main():
    st.title("ResumeMate - Smart Resume Builder 📝")

    # Collect user inputs
    name = st.text_input("Your Name")
    contact = st.text_input("Contact Number")
    email = st.text_input("Email Address")
    job_title = st.selectbox("Job Title", list(job_title_skills.keys()))
    experience = st.text_area("Experience")
    education = st.text_area("Education")
    certifications = st.text_area("Certifications")
    languages = st.text_area("Languages")

    skills = job_title_skills.get(job_title, [])

    # NEW: Template Choice
    template_choice = st.selectbox("Choose Resume Template", ["Classic Clean", "Professional Modern"])
    template_number = 1 if template_choice == "Classic Clean" else 2

    if st.button("Generate Resume"):
        resume_data = {
            "name": name,
            "contact": contact,
            "email": email,
            "job_title": job_title,
            "experience": experience,
            "skills": skills,
            "education": education,
            "certifications": certifications,
            "languages": languages
        }

        # Convert the resume for the job role
        converted_resume_data = convert_resume_for_job_role(job_title, resume_data)

        # Build resume text
        resume_text = build_resume(
            converted_resume_data["name"],
            converted_resume_data["contact"],
            converted_resume_data["email"],
            converted_resume_data["job_title"],
            converted_resume_data["experience"],
            converted_resume_data["skills"],
            converted_resume_data["education"],
            converted_resume_data["certifications"],
            converted_resume_data["languages"]
        )

        # Generate PDF with selected template
        pdf_output_path = generate_pdf(
            converted_resume_data["name"],
            converted_resume_data["contact"],
            converted_resume_data["email"],
            converted_resume_data["job_title"],
            converted_resume_data["experience"],
            converted_resume_data["skills"],
            converted_resume_data["education"],
            converted_resume_data["certifications"],
            converted_resume_data["languages"],
            template_choice=template_number  # <-- Important
        )

        if pdf_output_path:
            st.success("✅ Resume generated successfully!")
            st.text_area("Generated Resume", resume_text)
            with open(pdf_output_path, "rb") as file:
                st.download_button("📥 Download Resume", file, file_name=f"{name}_Resume.pdf", mime="application/pdf")

    st.divider()
    st.subheader("📋 ATS Resume Score Checker")

    job_keywords_input = st.text_area("Enter important job keywords (comma separated)", "")

    if st.button("Check ATS Score"):
        if job_keywords_input.strip():
            job_keywords = [word.strip() for word in job_keywords_input.split(",")]

            resume_path = f"outputs/{name}_Resume.pdf"
            if not os.path.exists(resume_path):
                st.error("⚠️ Please generate a resume first to check ATS Score.")
                return

            try:
                with open(resume_path, "rb") as f:
                    pdf_reader = PdfReader(f)
                    resume_text = ""
                    for page in pdf_reader.pages:
                        resume_text += page.extract_text()
            except Exception as e:
                st.error(f"⚠️ Error reading the resume PDF: {e}")
                return

            result = check_ats_score(resume_text, job_keywords)

            st.success(f"✅ Your ATS Score: {result['ats_percentage']}%")
            st.write("✅ Matched Keywords:", result["keywords_found"])
            st.write("❌ Missing Keywords:", result["keywords_missing"])
            if result["sections_missing"]:
                st.warning(f"⚠️ Missing Sections: {', '.join(result['sections_missing'])}")
        else:
            st.warning("⚠️ Please enter some keywords to check ATS score.")

    st.divider()
    st.subheader("🔍 Real-Time Job Search")

    job_title_input = st.text_input("Enter Job Title for Job Search (e.g., Frontend Developer)")
    location_input = st.text_input("Enter Location (or 'Remote')", value="Remote")
    num_pages = st.slider("Number of Pages to Search", 1, 5, 1)

    if st.button("Search Jobs"):
        if job_title_input.strip():
            with st.spinner('Fetching jobs...'):
                try:
                    jobs = search_jobs(job_title_input, location_input, num_pages)
                    if jobs:
                        st.success(f"Found {len(jobs)} jobs!")
                        for job in jobs:
                            st.subheader(job['Title'])
                            st.write(f"**Company:** {job['Company']}")
                            st.write(f"**Location:** {job['Location']}")
                            st.write(f"**Posted At:** {job['Posted']}")
                            st.markdown(f"[👉 Apply Here]({job['Job Link']})", unsafe_allow_html=True)

                            # Skill matching
                            if skills:
                                match_result = match_skills(skills, job['Title'] + " " + job.get('Description', ''))
                                st.info(f"✅ Skills Matched: {', '.join(match_result['matched_skills'])}")
                                st.warning(f"❌ Skills Missing: {', '.join(match_result['missing_skills'])}")

                            st.divider()
                    else:
                        st.warning("No jobs found for this query.")
                except Exception as e:
                    st.error(f"⚠️ Error fetching jobs: {e}")
        else:
            st.warning("⚠️ Please enter a job title to search.")

if __name__ == "__main__":
    main()
