import re
import io
import yaml
import shutil
from typing import Optional, Dict
from pathlib import Path
from datetime import datetime

#TODO: These belong in environment.config.py
DEFAULT_ROOT_DIRECTORY = Path.cwd() / "database"
DEFAULT_MIGRATIONS_DIRECTORY = DEFAULT_ROOT_DIRECTORY / "migrations"


class MigrationMetaData:

    def __init__(self, content: str) -> None:
        self._raw_meta = self.parse_meta_data(content)

        self.migration_name = self._raw_meta["migration_name"]
        self.created_at = self._raw_meta["created_at"]
        self.created_by = self._raw_meta["created_by"]
        self.team_name = self._raw_meta["team_name"]
        self.auto_commit = self._raw_meta.get("auto_commit", True) == "True"
        self.feature = self._raw_meta.get("feature")
        self.what = self._raw_meta.get("what")
        self.why = self._raw_meta.get("why")
        self.description = self._raw_meta.get("description")
        self.ticket = str(self._raw_meta.get("ticket"))

    @staticmethod
    def parse_meta_data(content: str) -> Dict[str, str]:
        meta_pattern = r"<meta>(.*?)</meta>"
        meta_content = re.search(meta_pattern, content, re.DOTALL).group(1)
        with io.StringIO() as buffer:
            buffer.write(meta_content)
            buffer.seek(0)
            return yaml.safe_load(buffer)


class Migration:

    def __init__(self, name: str, key: Optional[int] = None, migrations_directory: Optional[Path] = None) -> None:
        self.name = name
        self.key = key
        self.migrations_directory = migrations_directory or DEFAULT_MIGRATIONS_DIRECTORY

    @classmethod
    def from_filename(cls, filename: str):
        key, name = filename.replace(".sql", "").split("--")
        return cls(name=name, key=int(key))

    @property
    def filename(self) -> str:
        if not self.key:
            now = str(datetime.now().timestamp()).split(".")[0]
            return f"{now}--{self.name}.sql"
        return f"{self.key}--{self.name}.sql"

    @property
    def path(self) -> Path:
        return self.migrations_directory.joinpath(self.filename)

    @property
    def content(self) -> str:
        return self.path.read_text()

    def create(self, content: str) -> None:
        self.path.touch(exist_ok=True)
        self.path.write_text(content)

    def meta(self) -> MigrationMetaData:
        return MigrationMetaData(self.content)

    def up(self) -> str:
        return self.content.partition("--<migrate: up>")[2].partition("--<migrate: down>")[0]

    def down(self) -> str:
        return self.content.partition("--<migrate: down>")[2]


class DbSoupProject:

    def __init__(self) -> None:
        self.root_directory = DEFAULT_ROOT_DIRECTORY
        self.migrations_directory = DEFAULT_MIGRATIONS_DIRECTORY

    def init_project(self) -> None:
        self.root_directory.mkdir(exist_ok=True, parents=True)
        self.migrations_directory.mkdir(exist_ok=True, parents=True)

    def destroy_project(self) -> None:
        shutil.rmtree(self.root_directory, ignore_errors=True)

    def migrations(self) -> Dict[int, Migration]:
        migrations = {}
        for file in self.migrations_directory.glob("**/*.sql"):
            migration = Migration.from_filename(file.name)
            migrations[migration.key] = migration
        return migrations
