def match_skills(user_skills, job_description):
    matched_skills = [skill for skill in user_skills if skill.lower() in job_description.lower()]
    missing_skills = [skill for skill in user_skills if skill.lower() not in job_description.lower()]
    
    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }
