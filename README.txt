CURRENT FUNCTIONALITY:
Can add, delete, and update songs in Song table
Can login using username and password
Password is salted and hashed before inserted into database on signup

TO DO:
Input validation (inputting apostrophe causes server error because not escaped properly)
Need to implement 2 Advanced SQL Queries
Need to update login to use user e-mail instead of username
	(not an issue now, but if two users have same username and password could cause error)
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