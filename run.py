"""This file runs the whole app."""

from app.db.methods import *
import asyncio
from datetime import datetime
# from app.db.repository import *
dt = datetime(year=2024, month=3, day=31, hour=7, minute=0)

from app.db.repository import *

async def main():
    await drop_db()
    await init_db()


async def m1():
    hm = Home(None, dt)
    await hm.create()

    print(hm)

async def m2():
    fl = Floor(None, 2, 1)
    await fl.create()

    print(fl)

async def m3():
    ap = Apart(None, 1, 1)
    await ap.create()

    print(ap)


async def m4():
    w = Wind(None, False, 1)
    await w.create()

    print(w)


####################


async def d1():
    sm = await Home.get(1)

    print(sm)

    sm2 = await sm.get_floors()

    print(sm2)

    ap = await sm2[0].get_aparts()

    print(ap)

    wi = await ap[0].get_winds()

    print(wi)


async def d2():
    sm = ...

    print(sm)


async def d3():
    sm = ...

    print(sm)


async def d4():
    sm = ...

    print(sm)



asyncio.run(d1())
