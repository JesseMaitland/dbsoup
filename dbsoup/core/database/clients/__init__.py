import importlib
from dbsoup.core.database.connectivity import TypeDbClient


def get_db_client(dialect: str, connection_string: str) -> TypeDbClient:
    dot_path = f"dbsoup.core.database.clients.{dialect}_client"
    module = importlib.import_module(dot_path)
    return getattr(module, f"{dialect.capitalize()}Client")(connection_string=connection_string)
