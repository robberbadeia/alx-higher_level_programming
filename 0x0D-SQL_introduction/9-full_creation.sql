-- T09. Full creation
-- Script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

-- Create Table
CREATE TABLE IF NOT EXISTS 
    second_table(
        id INT,
        name VARCHAR(2560),
        score INT
    );

-- Insert Mltiple Rows
INSERT INTO second_table VALUES (1, "John", 10)
INSERT INTO second_table VALUES (2, "Alex", 3)
INSERT INTO second_table VALUES (3, "Bob", 14)
INSERT INTO second_table VALUES (4, "George", 8)

