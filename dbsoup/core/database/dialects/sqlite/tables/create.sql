CREATE TABLE IF NOT EXISTS migration_history
(
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    key           INTEGER,
    name          TEXT,
    created_by    TEXT,
    team_name     TEXT,
    feature       TEXT,
    what          TEXT,
    why           TEXT,
    description   TEXT,
    ticket        TEXT,
    method        TEXT,
    up            TEXT,
    down          TEXT
    executed_at   TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_migrations_key ON migration_history(key ASC);


CREATE TABLE IF NOT EXISTS applied_migrations
(
    key INTEGER PRIMARY KEY,
    executed_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_migrations_key ON applied_migrations(key ASC);
