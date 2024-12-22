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
            conn.execute("""
                CREATE TABLE IF NOT EXISTS menu (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    food_name TEXT,
                    price FLOAT,
                    description TEXT,
                    category TEXT)
                        """)
            conn.commit()

    def save_survey(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                INSERT INTO survey_results 
                (name, contact, food_rating, cleanliness_rating, extra_comments)
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

    def save_menu(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                INSERT INTO menu 
                (food_name, price, description, category)
                VALUES (?, ?, ?, ?)
                """,
                (
                    data.get("food_name"),
                    data.get("price"),
                    data.get("description"),
                    data.get("category")
                )
            )
            conn.commit()

    def get_menu_list(self):
        with sqlite3.connect(self.path) as conn:
            result = conn.execute("SELECT * from menu")
            result.row_factory = sqlite3.Row
            data = result.fetchall()
            # data = result.fetchmany(10)

            return [dict(row) for row in data]