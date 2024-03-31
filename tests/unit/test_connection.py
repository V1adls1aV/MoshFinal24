import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from tests.fixtures import db_test_session


@pytest.mark.asyncio
async def test_base(db_test_session: AsyncSession):
    ...

