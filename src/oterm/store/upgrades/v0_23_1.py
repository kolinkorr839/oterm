from collections.abc import Awaitable, Callable
from pathlib import Path

import aiosqlite


async def add_prompt_template_column(db_path: Path) -> None:
    async with aiosqlite.connect(db_path) as connection:
        cols = await connection.execute_fetchall("PRAGMA table_info(chat)")
        col_names = {row[1] for row in cols}
        if "prompt_template" not in col_names:
            await connection.execute(
                "ALTER TABLE chat ADD COLUMN prompt_template TEXT"
            )
            await connection.commit()


upgrades: list[tuple[str, list[Callable[[Path], Awaitable[None]]]]] = [
    ("0.23.2", [add_prompt_template_column]),
]
