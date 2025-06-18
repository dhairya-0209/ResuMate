import re

# Define required sections and keywords based on your provided resume
REQUIRED_SECTIONS = [
    "Profile", "Areas of Expertise", "Professional Experience", "Education",
    "Certifications", "Skills", "Languages"
]

# Example of job-specific keywords to match
REQUIRED_KEYWORDS = [
    "Python", "Blockchain", "Google Cloud", "GitHub", "Azure", "SQL", "HTML", "CSS", "AI",
    "Machine Learning", "Problem-Solving", "System Design", "Web Development", "Leadership",
    "Communication", "Creative Problem-Solving", "Teamwork", "Adaptability", "Analytical Thinking"
]

def check_ats_score(resume_text, job_keywords=None):
    """
    Function to check ATS score based on required sections and keywords.
    
    Parameters:
    resume_text (str): The content of the resume to be checked.
    job_keywords (list): List of keywords specific to the job role.

    Returns:
    dict: ATS score, missing sections, and matched/missing keywords.
    """
    resume_text_lower = resume_text.lower()
    section_score = 0
    missing_sections = []

    # 1. Check for required sections in the resume
    for section in REQUIRED_SECTIONS:
        if section.lower() in resume_text_lower:
            section_score += 1
        else:
            missing_sections.append(section)

    # 2. Check for keywords from the job (or use default keywords)
    keyword_found = []
    keyword_missing = []

    keywords_to_check = job_keywords if job_keywords else REQUIRED_KEYWORDS

    for keyword in keywords_to_check:
        pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
        if re.search(pattern, resume_text_lower):
            keyword_found.append(keyword)
        else:
            keyword_missing.append(keyword)

    keyword_score = len(keyword_found)

    # 3. Calculate total ATS score
    total_possible = len(REQUIRED_SECTIONS) + len(keywords_to_check)
    obtained_score = section_score + keyword_score
    ats_percentage = int((obtained_score / total_possible) * 100)

    # 4. Result dictionary with sections and keywords analysis
    result = {
        "ats_percentage": ats_percentage,
        "sections_missing": missing_sections,
        "keywords_found": keyword_found,
        "keywords_missing": keyword_missing
    }

    return result


# Example Usage

resume_sample = """
Komal Bhardwaj Software Developer
H: +91 8397046110 | E: komalbhardwaj0302@gmail.com | LinkedIn | GitHub

Profile:
Proficient software developer with 6+ months of experience as a Cloud and AI Intern, pursuing a Bachelor's in Computer Science. Skilled in Python. Actively contributing to tech projects and extracurricular activities, demonstrating a strong commitment to innovation.

Areas of Expertise:
• Python
• Blockchain
• Google Cloud Platform
• GitHub

Professional Experience:
Cloud Intern – Cyberent Cube, Faridabad, India
March 2024 – June 2024
• Implemented Google Cloud services for real-world web development projects, focusing on deployment and management of web applications.
• Integrated databases, storage solutions, and computing resources into web applications, ensuring seamless functionality and performance.
• Delivered scalable, secure, and optimized cloud-based solutions, meeting client specifications and project timelines effectively.

AI Developer – RYM Grenergy Solutions, Gurugram, India
May 2024 – July 2024
• Trained AI models and managed datasets for various applications.
• Leveraged databases for storing and managing training data, ensuring data integrity and accessibility.
• Developed and optimized AI models, focusing on accuracy, efficiency, and scalability to meet project goals and client requirements.

AI Trainee – Honeywell, Faridabad, India
March 2024 – April 2024
• Trained AI models using Azure services and managed datasets.
• Utilized Azure databases to store and manage training data, ensuring integrity and accessibility.
• Developed and optimized AI models on Azure to meet project goals, with a focus on accuracy and efficiency.

Google Cloud Lead – GDSC ACEM, Faridabad, India
August 2023 – May 2024
• Led projects on Google Cloud, including application deployment and data management.
• Trained and mentored students to develop and optimize solutions on Google Cloud with a focus on scalability and efficiency.

Education:
Bachelor of Technology (B.Tech) – JC Bose University of Science and Technology, Faridabad
2022 – 2026
• Specialization: Computer Science Engineering with a focus on AI and ML
• CGPA: 8.3

Certifications:
• Career Essentials in Generative AI – LinkedIn, July 2024
• Generative AI – Google, May 2024
• Google Cloud – Google, September 2023
• Information Management System – NPTEL, October 2023

Skills:
• Python, GitHub, OpenAI, Azure, SQL, HTML, CSS
• Proficient in problem-solving, system design, and web development

Soft Skills:
• Presentation, Planning, Creative Problem-Solving, Teamwork
• Adaptability, Analytical Thinking, Leadership, Communication

Languages:
• English
• Hindi
"""

result = check_ats_score(resume_sample)
print(f"ATS Score: {result['ats_percentage']}%")
print(f"Sections Missing: {', '.join(result['sections_missing']) if result['sections_missing'] else 'None'}")
print(f"Matched Keywords: {', '.join(result['keywords_found']) if result['keywords_found'] else 'None'}")
print(f"Missing Keywords: {', '.join(result['keywords_missing']) if result['keywords_missing'] else 'None'}")
