-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id, cities.name -- Query to list all the cities from California
FROM cities
WHERE cities.state_id = ( -- Query to get the id of California
      SELECT id
      FROM states
      WHERE name = "California");