# utils/resume_builder.py

def build_resume(name, contact, email, job_title, experience, skills, education, certifications, languages):
    # Safety checks: if any field is blank, put placeholder
    name = name.strip() or "Your Name"
    contact = contact.strip() or "Your Phone Number"
    email = email.strip() or "your.email@example.com"
    job_title = job_title.strip() or "Your Job Title"
    experience = experience.strip() or "Describe your profile, experience and goals here."
    education = education.strip() or "Your Educational Background"
    certifications = certifications.strip() or "Your Certifications & Courses"
    languages = languages.strip() or "Languages you know"

    # Check if skills is a list, else convert it into one
    if isinstance(skills, list):
        skills = list(set(skills))  # Remove duplicates
    else:
        skills = skills.split(",")  # If skills is a comma-separated string, split into a list.
    skills_text = ", ".join(skills) if skills else "Your Skills"

    # Build the resume
    resume = f"""
Resume
{name}
{job_title}
Phone: {contact} | Email: {email}

Profile
{experience}

Areas of Expertise
{skills_text}

Education
{education}

Certifications
{certifications}

Languages
{languages}
"""
    return resume.strip()

# Example test
resume = build_resume(
    name="Komal Bhardwaj",
    contact="123-456-7890",
    email="komal@example.com",
    job_title="Software Engineer",
    experience="Experience in AI and Cloud development.",
    skills=["Python", "Java", "Problem Solving"],
    education="B.Tech in Computer Science",
    certifications="Generative AI, Google Cloud",
    languages="English, Hindi"
)

print(resume)
