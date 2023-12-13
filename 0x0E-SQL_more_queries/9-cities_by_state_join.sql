-- T09. Cities by States
-- Script that lists all cities contained in the database hbtn_0d_usa.
SELECT 
    id,
    cities.name,
    states.name
FROM
    states 
    FULL OUTER JOIN
    cities
ON
    states.id = cities.state_id;
