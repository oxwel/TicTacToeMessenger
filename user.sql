CREATE TABLE user (
        id INTEGER NOT NULL,
        fb_id INTEGER,
        wins INTEGER,
        losses INTEGER,
        ties INTEGER,
        games INTEGER,
        PRIMARY KEY (id),
        UNIQUE (fb_id)
);
