# main.py

from fastapi import FastAPI, HTTPException
from jsearch_api.jsearch_client import search_jobs

app = FastAPI()

@app.get("/search-jobs/")
def get_jobs(query: str, location: str = "Remote", num_pages: int = 1):
    try:
        jobs = search_jobs(query, location, num_pages)
        return {"jobs": jobs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
