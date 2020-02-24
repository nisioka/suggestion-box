drop table if exists suggestions;
create table suggestions
(
    `id`             integer primary key autoincrement,
    `title_en`       text not null,
    `title_ja`       text not null,
    `description_en` text not null,
    `description_ja` text not null,
    `author`         text not null,
    `created`        datetime default CURRENT_TIMESTAMP
);
CREATE INDEX index_created ON suggestions (created);