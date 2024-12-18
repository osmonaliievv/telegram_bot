import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS survey_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    contact TEXT,
                    food_rating INTEGER,
                    cleanliness_rating INTEGER,
                    extra_comments TEXT
                )
            """)
            conn.commit()

    def save_survey(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                INSERT INTO survey_results (name, contact, food_rating, cleanliness_rating, extra_comments)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    data.get("name"),
                    data.get("contact"),
                    int(data.get("food_rating")),
                    int(data.get("cleanliness_rating")),
                    data.get("extra_comments")
                )
            )
            conn.commit()
