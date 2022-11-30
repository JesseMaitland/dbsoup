from typing import List
from dbsoup.core.database.connectivity import TypeDbClient
from dbsoup.core.project import DbSoupProject


def execute_migrations_up(db_client: TypeDbClient, dbsoup_project: DbSoupProject, applied_migrations: List[int]) -> None:

    for migration in dbsoup_project.migrations_to_apply(applied_migrations):
        db_client.execute_statement(migration.up())

        db_client.execute_statement(
            db_client.dialect.insert_applied_migration,
            migration.key
        )

        db_client.execute_statement(
            db_client.dialect.insert_migration_history,
            **migration.get_migration_table_insert_args("up")
        )


def execute_migration_down(db_client: TypeDbClient, dbsoup_project: DbSoupProject, applied_migrations: List[int]) -> None:

    for migration in dbsoup_project.migrations_to_apply(applied_migrations):
        db_client.execute_statement(migration.up())

        db_client.execute_statement(
            db_client.dialect.insert_applied_migration,
            migration.key
        )

        db_client.execute_statement(
            db_client.dialect.insert_migration_history,
            **migration.get_migration_table_insert_args("up")
        )
