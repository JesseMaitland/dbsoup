/*<meta>

migration_name: {{name}}
created_at: {{date}}
created_by: {{user}}
team_name:
auto_commit: True

feature: what feature is your migration used for?
what: what your migration is doing
why: why you need to alter this table

description: |
    put your description here about how your migration works, and perhaps what other things is needs to do

links:
  - www.link-to-some-ticket.com
  - some other link to documentation

</meta>*/

--<migrate: up>
-- write the migrate up ddl / dml here using plain sql
CREATE TABLE IF NOT EXISTS foo(
    col1 INT,
    col2 VARCHAR(128)
);


--<migrate: down>
-- write the migrate down ddl / dms here using plain sql
DROP TABLE IF EXISTS foo;


