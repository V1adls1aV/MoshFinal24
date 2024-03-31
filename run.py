"""This file runs the whole app."""

from app.db.methods import *
import asyncio

async def main():
    await init_db()

asyncio.run(main())
