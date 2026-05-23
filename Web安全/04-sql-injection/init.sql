CREATE DATABASE IF NOT EXISTS ctf;
USE ctf;

CREATE TABLE IF NOT EXISTS users (
    id       INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(64),
    password VARCHAR(64),
    flag     VARCHAR(256)
);

INSERT IGNORE INTO users (username, password, flag) VALUES ('alice', 'password123', '');
INSERT IGNORE INTO users (username, password, flag) VALUES ('admin', 'sup3rs3cr3t!', 'flag{TEST_Dynamic_FLAG}');
