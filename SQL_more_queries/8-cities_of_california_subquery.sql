-- list of cities of California
SELECT cities.id, cities.name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id;
