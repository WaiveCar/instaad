CREATE TABLE user
(
        email VARCHAR(50),
        paid_user BOOLEAN DEFAULT 'True',
        id INTEGER NOT NULL AUTO_INCREMENT,
        instagram VARCHAR(30),
        password VARCHAR(60),
        PRIMARY KEY (id),
        UNIQUE (email),
        CHECK (paid_user IN (0, 1))
);
CREATE TABLE campaign
(
        date_paid DATETIME,
        date_registered DATETIME NOT NULL,
        date_started DATETIME,
        id INTEGER NOT NULL AUTO_INCREMENT,
        last_city VARCHAR(25),
        paid BOOLEAN,
        user_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        CHECK (paid IN (0, 1)),
        FOREIGN KEY(user_id) REFERENCES user (id)
);
