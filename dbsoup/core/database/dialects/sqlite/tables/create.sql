CREATE TABLE IF NOT EXISTS migrations
(
    id          INT IDENTITY,
    name        VARCHAR(128),
    content     TEXT,
    applied_at  TIMESTAMP DEFAULT CURRENT_DATE
);


CREATE TABLE IF NOT EXISTS history
(
    id          INT IDENTITY,
    name        VARCHAR(128),
    content     TEXT,
    method      VARCHAR(128),
    applied_at  TIMESTAMP DEFAULT CURRENT_DATE
);
