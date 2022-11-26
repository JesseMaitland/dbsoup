CREATE TABLE IF NOT EXISTS dbsoup.migrations
(
    id          INT IDENTITY,
    name        VARCHAR(128),
    content     TEXT,
    applied_at  TIMESTAMP DEFAULT CURRENT_DATE

);
