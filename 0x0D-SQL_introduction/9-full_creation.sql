-- T09. Full creation
-- Script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

-- Create Table
CREATE TABLE IF NOT EXISTS second_table (
        id INT,
        name VARCHAR(2560),
        score INT
    );
-- Insert Mltiple Rows
INSERT INTO
    second_table
VALUES
    (1, "John", 10)و
    (2, "Alex", 3)و
    (3, "Bob", 14)و
    (4, "George", 8)
