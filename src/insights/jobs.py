from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path) as file:
        content = csv.DictReader(file)
        jobs = [job for job in content]

    return jobs


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs = read(path)
    set_job_types = set()
    for job in jobs:
        set_job_types.add(job["job_type"])
    return set_job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    # o if deve ler cada item no momento que ele é iterado,
    # não ler a lista jobs de uma vez só, não fazer o if em cima de jobs.
    # types = []
    # for typ in jobs:
    #     if typ["job_type"] == job_type:
    #         types.append(typ)
    return [types for types in jobs if types["job_type"] == job_type]
