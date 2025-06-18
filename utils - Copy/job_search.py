# utils/job_search.py

import requests

# RapidAPI Constants
RAPIDAPI_KEY = "29e0624048mshedc23f71cdd2943p17e502jsnbff3d09d59b9"
RAPIDAPI_HOST = "jsearch.p.rapidapi.com"
BASE_URL = "https://jsearch.p.rapidapi.com/search"

# Function to search jobs
def search_jobs(query, location="Remote", num_pages=1):
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }
    params = {
        "query": query,
        "location": location,
        "num_pages": num_pages
    }

    try:
        response = requests.get(BASE_URL, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            jobs = data.get('data', [])
            return jobs
        else:
            print(f"Error: {response.status_code}")
            return []
    except Exception as e:
        print(f"Exception occurred: {e}")
        return []

# Helper function to format job results
def format_job_results(jobs):
    formatted_jobs = []
    for job in jobs:
        job_info = {
            "Title": job.get("job_title"),
            "Company": job.get("employer_name"),
            "Location": job.get("job_city"),
            "Job Link": job.get("job_apply_link"),
            "Posted": job.get("job_posted_at_datetime_utc"),
        }
        formatted_jobs.append(job_info)
    return formatted_jobs
