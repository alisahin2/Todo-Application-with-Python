# tum todos tablosunu secer
SELECT  * from todos

# todos tablosuna yeni bir oge eklemeyi saglar
INSERT INTO todos
(userId,name,description,time)
VALUES ('4','konser',' hayko','2021-1-13 20:30')

# todos tablosundan id=6 ve userId=3 olan ogenin bilgilerini guncellemeyi saglar
UPDATE todos
SET name='piknik',
	description='ailecek piknik',
    time='2221-10-10'
WHERE id= '6' AND userId='3'

#todos tablosundan id=3 olani siler
DELETE from todos
Where id='3'