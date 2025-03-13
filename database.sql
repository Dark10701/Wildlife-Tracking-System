CREATE DATABASE IF NOT EXISTS wildlife_tracking;
USE wildlife_tracking;

CREATE TABLE Animals (
    animal_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    species VARCHAR(100),
    status ENUM('Endangered', 'Vulnerable', 'Safe'),
    habitat_id INT
);

CREATE TABLE Habitats (
    habitat_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(255),
    climate VARCHAR(100)
);

CREATE TABLE Tracking_Data (
    track_id INT AUTO_INCREMENT PRIMARY KEY,
    animal_id INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    FOREIGN KEY (animal_id) REFERENCES Animals(animal_id)
);
