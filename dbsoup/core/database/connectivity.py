from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, TypeVar

SQL_DIALECTS_PATH = Path(__file__).absolute().parent / "dialects"


class SqlDialect:

    def __init__(self, dialect: str) -> None:
        self.dialect = dialect
        self.dialect_path = SQL_DIALECTS_PATH / self.dialect

    @property
    def create_schema(self) -> str:
        return self.dialect_path.joinpath("schema/create.sql").read_text()

    @property
    def drop_schema(self) -> str:
        return self.dialect_path.joinpath("schema/drop.sql").read_text()

    @property
    def create_tables(self) -> str:
        return self.dialect_path.joinpath("tables/create.sql").read_text()

    @property
    def drop_tables(self) -> str:
        return self.dialect_path.joinpath("tables/drop.sql").read_text()


class BaseDbClient(ABC):

    def __init__(self, dialect: SqlDialect, connection_string: str) -> None:
        self.dialect = dialect
        self.connection_string = connection_string

    @abstractmethod
    def get_connection(self) -> Any:
        pass

    @abstractmethod
    def execute_ddl(self, ddl: str) -> None:
        pass

    @abstractmethod
    def init_db(self) -> None:
        pass

    @abstractmethod
    def destroy_db(self) -> None:
        pass

    def create_schema(self) -> None:
        self.execute_ddl(self.dialect.create_schema)

    def drop_schema(self) -> None:
        self.execute_ddl(self.dialect.drop_schema)

    def create_tables(self) -> None:
        for ddl in self.dialect.create_tables.split(";"):
            ddl = ddl.strip()
            if ddl:
                ddl = f"{ddl};"
                print(ddl)
                self.execute_ddl(ddl)

    def drop_tables(self) -> None:
        for ddl in self.dialect.drop_tables.split(";"):
            ddl = ddl.strip()
            if ddl:
                ddl = f"{ddl};"
                print(ddl)
                self.execute_ddl(ddl)


TypeDbClient = TypeVar('TypeDbClient', bound=BaseDbClient)
