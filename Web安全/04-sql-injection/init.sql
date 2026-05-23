ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS ctfdb;
USE ctfdb;

CREATE TABLE IF NOT EXISTS users (
    id       INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(64),
    password VARCHAR(64),
    flag     VARCHAR(256)
);

-- 普通用户（无 flag）
INSERT IGNORE INTO users (username, password, flag) VALUES ('alice', 'password123', '');
-- admin 用户持有 flag（从环境变量注入，见 entrypoint.sh）
INSERT IGNORE INTO users (username, password, flag) VALUES ('admin', 'sup3rs3cr3t!', 'FLAG_PLACEHOLDER');
-- 更新 flag（每次启动都更新，确保动态 FLAG 生效）
UPDATE users SET flag='FLAG_PLACEHOLDER' WHERE username='admin';
