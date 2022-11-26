from argparse import Namespace
from dbsoup.environment.variables import DBSOUP_DIALECT, DBSOUP_CONNECTION_STRING
from dbsoup.core.database.clients import get_db_client


__version__ = "0.0.0"

db_client = get_db_client(DBSOUP_DIALECT, DBSOUP_CONNECTION_STRING)


def init(cmd: Namespace) -> None:
    print("Initializing database for use with dbsoup.")
    db_client.init_db()


def destroy(cmd: Namespace) -> None:
    print("Destroying dbsoup database")
    db_client.destroy_db()


def new(cmd: Namespace) -> None:
    print("new command")


def up(cmd: Namespace) -> None:
    print("up command")


def down(cmd: Namespace) -> None:
    print("down command")


def version(cmd: Namespace) -> None:
    print(f"dbsoup -- Migrations Made Simple -- Version: {__version__}")
