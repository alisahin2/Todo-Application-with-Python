# tum users tablosunu secer
SELECT  * from users

# users tablosuna yeni bir user tanimlamayi saglar
INSERT INTO users
(name,surname,email,city,birthday,password)
VALUES ('semsa','sahinn','sem@g.com','xxx','1992-12-12', 12345)

# users tablosundan id=2 olanin bilgilerini guncellemeyi saglar
UPDATE users
SET name='2',
	surname='2',
    city='2',
	email='2',
    birthday='2222-12-12',
    password='2'
WHERE id='2'

#users tablosundan id=2 olani siler
DELETE from users
Where id='2'