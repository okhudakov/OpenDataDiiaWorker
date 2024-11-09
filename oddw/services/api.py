import datetime as dt
from itertools import chain
import asyncio
import requests
import os
import sys
sys.path.append(os.getcwd())
from oddw.settings import env
from oddw.utils import flatten


def _get_tasks(s, urls):
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(s.get(url)))
    return tasks


def get_rsa_reports(result=None, url=None):
    if result is None:
        result = []
    if url is None:
        now = dt.datetime.now()

        quarter_of_the_year = (now.month - 1) // 3 + 1
        year = now.year

        url = (
            f"{env['BASE_RSA_REPORT_URL']}"
            f"{year if quarter_of_the_year != 1 else (year - 1)}/"
            f"{(quarter_of_the_year - 1) if quarter_of_the_year != 1 else 4}?format=json"
        )

    rsa_reports_response = requests.get(url)
    rsa_reports = rsa_reports_response.json()

    result.append(rsa_reports["results"])

    return (
        flatten(result)
        if rsa_reports["next"] is None
        else get_rsa_reports(result, rsa_reports["next"])
    )


async def get_entries_reports_ids(s, report_ids, results=None, urls=None):
    if results is None:
        results = []

    if urls is None:
        urls = [
            f"{env['BASE_ENTRY_REPORT_URL']}{report_id}?format=json"
            for report_id in report_ids
        ]

    tasks = _get_tasks(s, urls)

    responses = await asyncio.gather(*tasks)

    urls = []
    for response in responses:
        entry_report = await response.json()

        if entry_report["next"] is not None:
            urls.append(entry_report["next"])
        results.append(result["id"] for result in entry_report["results"])

    return (
        chain(*results)
        if not urls
        else await get_entries_reports_ids(s, report_ids, results, urls)
    )


async def get_detail_reports(s, report_entries_ids):
    urls = [
        f"{env['BASE_DETAIL_REPORT_URL']}{report_entry_id}"
        for report_entry_id in report_entries_ids
    ]

    tasks = _get_tasks(s, urls)
    end_r = []
    responses = await asyncio.gather(*tasks)
    for resp in responses:
        end_r.append(await resp.json())

    return end_r
