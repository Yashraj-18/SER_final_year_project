DROP DATABASE IF EXISTS emotion_recognition;
CREATE DATABASE emotion_recognition;
USE emotion_recognition;

CREATE TABLE register (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(225), 
    email VARCHAR(225), 
    pwd VARCHAR(225),
    cpwd VARCHAR(225)
);
