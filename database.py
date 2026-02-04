import aiosqlite


async def get_drug_data(title: str = None, column: str = "adult_dosage"):
    async with aiosqlite.connect("drugs.db") as db:
        async with db.execute(f"SELECT {column} FROM table_molecule_info WHERE title LIKE ?", (f"%{title}%",)) as cursor:
            return await cursor.fetchone()