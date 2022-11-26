import shutil
from pathlib import Path


class DbSoupProject:

    def __init__(self) -> None:
        self.root_directory = Path.cwd() / "database"
        self.migrations_directory = self.root_directory / "migrations"

    def init_project(self) -> None:
        self.root_directory.mkdir(exist_ok=True, parents=True)
        self.migrations_directory.mkdir(exist_ok=True, parents=True)

    def destroy_project(self) -> None:
        shutil.rmtree(self.root_directory, ignore_errors=True)
