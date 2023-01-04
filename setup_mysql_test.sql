-- Mysql script that connects to the database
-- Copyright © baccrie & Temi

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO hbnb_test@localhost WITH GRANT OPTION;
GRANT SELECT ON performance_schema . * TO hbnb_dev@localhost WITH GRANT OPTION;
