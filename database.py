import aiosqlite


async def get_drug_data(title, column):
    async with aiosqlite.connect("drugs.db") as db:
        async with db.execute(f"SELECT {column} FROM medications WHERE title LIKE ?", (f"%{title}%",)) as cursor:
            return await cursor.fetchone()