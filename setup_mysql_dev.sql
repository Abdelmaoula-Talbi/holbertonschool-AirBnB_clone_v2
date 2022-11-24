-- script that prepares a MySQL server for the project
CREATE DATABASE	IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db.* TO hbnb_dev;
GRANT SELECT ON performance_shema TO hbnb_dev;
