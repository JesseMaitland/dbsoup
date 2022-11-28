import getpass
from datetime import datetime
from argparse import Namespace
from dbsoup.environment import TemplateLoader
from dbsoup.environment.variables import DBSOUP_DIALECT, DBSOUP_CONNECTION_STRING
from dbsoup.core.database.clients import get_db_client
from dbsoup.core.project import DbSoupProject, Migration


__version__ = "0.0.0"


db_client = get_db_client(DBSOUP_DIALECT, DBSOUP_CONNECTION_STRING)
dbsoup_project = DbSoupProject()
template_loader = TemplateLoader()


def init(cmd: Namespace) -> None:
    print("Initializing database for use with dbsoup.")
    db_client.init_db()
    print("Creating dbsoup directories")
    dbsoup_project.init_project()


def destroy(cmd: Namespace) -> None:
    print("Destroying dbsoup database")
    db_client.destroy_db()
    print("Destroying dbsoup directories")
    dbsoup_project.destroy_project()


def new(cmd: Namespace) -> None:
    migration = Migration(name=cmd.name)

    params = {
        "name": migration.name,
        "date": datetime.now().isoformat(sep=" ", timespec="seconds"),
        "user": getpass.getuser()
    }

    content = template_loader.get_template("migration.template.sql")
    migration.create(content.render(**params))


def up(cmd: Namespace) -> None:
    print("up command")
    migrations = dbsoup_project.migrations()
    results = db_client.execute_query(db_client.dialect.migrations)
    print(results)
    exit()
    m = migrations[1669617573]

    t = template_loader.get_template("sqlite/insert/migrations.sql")
    c = t.render(migration=m)
    print(c)
    db_client.execute_statement(c)


def down(cmd: Namespace) -> None:
    print("down command")


def version(cmd: Namespace) -> None:
    print(f"dbsoup -- Migrations Made Simple -- Version: {__version__}")
