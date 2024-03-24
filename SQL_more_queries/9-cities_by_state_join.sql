-- list records using 2 table data
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = cities.id;
