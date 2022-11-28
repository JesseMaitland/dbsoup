import sqlite3
from contextlib import closing
from typing import Any, Tuple
from dbsoup.core.database.connectivity import BaseDbClient, SqlDialect


class SqliteClient(BaseDbClient):

    def __init__(self, connection_string: str) -> None:
        dialect = SqlDialect(dialect="sqlite")
        super().__init__(dialect=dialect, connection_string=connection_string)

    def get_connection(self) -> Any:
        return sqlite3.connect(self.connection_string)

    def execute_statement(self, statement: str) -> None:
        with self.get_connection() as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(statement)
                connection.commit()

    def execute_query(self, query: str) -> Tuple[Any]:
        with self.get_connection() as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(query)
                return cursor.fetchall()

    def init_db(self) -> None:
        self.create_tables()

    def destroy_db(self) -> None:
        self.drop_tables()
