CURRENT FUNCTIONALITY:
Can add, delete, and update songs in Song table
Can login using email and password
Password is salted and hashed before inserted into database on signup
Entire database can be reset on request (heroku run init)

TO DO:
Input validation (inputting apostrophe causes server error because not escaped properly)
Need to implement 2 Advanced SQL Queries
Songs should not be input by users, but rather pulled using Soundcloud API
Need Playlist functionality (users should be able to add and remove songs from playlist)
Song table should update periodically on its own

Advanced SQL Query #1:
(orders song titles in user's playlist according to # of Soundcloud favorites)
SELECT Title 
FROM Song 
WHERE Song_Url=(SELECT Song_Url 
	FROM Playlist 
	WHERE Email=(SELECT Email
		FROM User
		WHERE Username='USERNAME_FROM_SESSION_COOKIE'))
ORDER BY Soundcloud_Favorites DESC

Advanced SQL Query #2:
(to do)