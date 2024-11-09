from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os
import sys

sys.path.append(os.getcwd())
from oddw.settings import db_uri

engine = create_async_engine(
    f"postgresql+asyncpg://{db_uri}",
    echo=True,
)

async_session = async_sessionmaker(engine, expire_on_commit=False)

