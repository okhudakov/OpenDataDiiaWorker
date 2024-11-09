import asyncio
import aiohttp

from services.api import (
    get_entries_reports_ids,
    get_detail_reports,
    get_rsa_reports,
)
from services.db import merge_report_details
from utils import benchmark_start, benchmark_end


async def main():
    rsa_reports = get_rsa_reports()
    rsa_reports_ids = [rsa_report["id"] for rsa_report in rsa_reports]

    async with aiohttp.ClientSession() as session:
        entires_report_ids = await get_entries_reports_ids(session, rsa_reports_ids)

        detail_reports = await get_detail_reports(session, entires_report_ids)

        await merge_report_details(detail_reports)


if __name__ == "__main__":
    benchmark_data = benchmark_start()

    asyncio.run(main())

    benchmark_end(benchmark_data)
