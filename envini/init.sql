create database if not exists cmcs;
use cmcs;
drop table if exists users;
CREATE TABLE users (
    uid INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    firstname VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL,
    tel VARCHAR(20) NOT NULL,
    cars VARCHAR(100) NOT NULL
);

drop table if exists cars;
CREATE TABLE cars (
    cid INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    carname VARCHAR(100) NOT NULL,
    info VARCHAR(1000) NOT NULL,
    tasks VARCHAR(100) NOT NULL
);

drop table if exists tasks;
CREATE TABLE tasks (
    tid INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    taskname VARCHAR(100) NOT NULL,
    info VARCHAR(1000) NOT NULL,
    status VARCHAR(20) NOT NUll
);