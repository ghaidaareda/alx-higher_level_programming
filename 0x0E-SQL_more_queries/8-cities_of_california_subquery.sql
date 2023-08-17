-- lists all the cities of California that can be found in the database

SELECT DISTINCT cities.id, cities.name FROM cities, states 
WHERE states.name = 'California'
ORDER BY cities.id ASC;
