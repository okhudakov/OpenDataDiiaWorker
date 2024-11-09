import uuid

from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func


Base = declarative_base()


class Record(Base):
    __tablename__ = "records"

    uid = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=True
    )
    idf = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    asc_org = Column(String, nullable=False)
    general_data = Column(String, nullable=False)
    activity_data = Column(String, nullable=False)
    info_support_data = Column(String, nullable=False)
    admin_service_data = Column(String, nullable=False)
    resp_person_data = Column(String, nullable=False)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=True
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=True,
    )
    deleted_at = Column(DateTime(timezone=True), nullable=True)
