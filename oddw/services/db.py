import json
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, and_, select
import asyncio
import os
import sys

sys.path.append(os.getcwd())
from oddw.db.session import async_session, engine
from oddw.db.models import Record
from oddw.utils import omit_if_none


class DBService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_update_record(self, model, **atts):
        try:
            new_item = model(**omit_if_none(atts))

            query = (
                select(Record)
                .where(Record.idf == new_item.idf)
            )
            result = await self.db_session.execute(query)
            record = result.scalars().first()

            if not record:
                self.db_session.add(new_item)
                await self.db_session.flush()

                return new_item

            query = (
                update(Record)
                .where(and_(Record.idf == new_item.idf, Record.deleted_at == None))
                .values(omit_if_none(atts))
                .returning(Record)
            )

            update_response = await self.db_session.execute(query)
            updated = update_response.fetchone()
            if updated is not None:
                return updated[0]
        except:
            print("error")


async def test_func(record):
    async with async_session() as db_session:
        async with db_session.begin():
            db = DBService(db_session)
            await db.create_update_record(Record, **{
                "idf": record["results"][0]["asc_org"]["idf"],
                "name": record["results"][0]["asc_org"]["name"],
                "asc_org": json.dumps(record["results"][0]["asc_org"]),
                "general_data": json.dumps(
                    record["results"][0]["general_data"]
                ),
                "activity_data": json.dumps(
                    record["results"][0]["activity_data"]
                ),
                "info_support_data": json.dumps(
                    record["results"][0]["info_support_data"]
                ),
                "admin_service_data": json.dumps(
                    record["results"][0]["admin_service_data"]
                ),
                "resp_person_data": json.dumps(
                    record["results"][0]["resp_person_data"]
                ),
            })


async def merge_report_details(records):
    async with engine.begin() as conn:
        tasks = [
            asyncio.create_task(
                test_func(record)
            )
            for record in records
        ]

        responses = await asyncio.gather(*tasks)
        ress = []
        for response in responses:
            if response is not None:
                ress.append(await response.json())

