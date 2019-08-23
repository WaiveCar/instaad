CREATE TABLE user
(
        email VARCHAR(50),
        paid_user BOOLEAN DEFAULT '0',
        id INTEGER NOT NULL AUTO_INCREMENT,
        password VARCHAR(60),
        PRIMARY KEY (id),
        UNIQUE (email),
        CHECK (paid_user IN (0, 1))
);
CREATE TABLE campaign
(
        date_registered DATETIME DEFAULT NOW(),
        id INTEGER NOT NULL AUTO_INCREMENT,
	ig_username VARCHAR(30) UNIQUE,
        last_city VARCHAR(25),
	lat DECIMAL(10,7),
	lng DECIMAL(10,7),
        paid BOOLEAN DEFAULT '0',
	sett_business VARCHAR(20),
	sett_control_content BOOLEAN,
	sett_social VARCHAR(20),
        user_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        CHECK (paid IN (0, 1)),
        FOREIGN KEY(user_id) REFERENCES user (id)
);
