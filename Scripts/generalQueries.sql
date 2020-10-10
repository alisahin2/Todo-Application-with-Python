# tum todolari listeleyen query
SELECT todos.id, users.name, users.surname, users.email, users.city, todos.name AS 'todo name', todos.description AS 'todo description'
FROM users
INNER JOIN todos ON todos.userId = users.id

# id numarasi 4 olan elemanin yaptigi isleri asagidaki parametrelere gore listeleyen query
SELECT todos.id, users.name, users.surname, users.email, users.city, todos.name AS 'todo name', todos.description AS 'todo description'
FROM users
INNER JOIN todos ON todos.userId = users.id WHERE users.id = 4