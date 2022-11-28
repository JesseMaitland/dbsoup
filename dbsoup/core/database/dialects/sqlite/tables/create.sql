CREATE TABLE IF NOT EXISTS migrations
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
    up            TEXT,
    down          TEXT
    executed_at   TEXT DEFAULT CURRENT_TIMESTAMP
);


CREATE INDEX IF NOT EXISTS idx_migrations_key ON migrations(key ASC);
