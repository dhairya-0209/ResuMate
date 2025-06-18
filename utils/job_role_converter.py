# utils/job_role_converter.py

def convert_resume_for_job_role(job_title, resume_data):
    # This is a simple example; modify as needed for specific job roles
    if job_title == "Data Scientist":
        resume_data["skills"].append("Machine Learning")
        resume_data["skills"].append("Data Analysis")
    elif job_title == "Software Engineer":
        resume_data["skills"].append("Problem-Solving")
        resume_data["skills"].append("System Design")
    elif job_title == "Cloud Engineer":
        resume_data["skills"].append("Cloud")
        resume_data["skills"].append("Azure")
    # Add more job role-specific modifications as needed
    return resume_data
