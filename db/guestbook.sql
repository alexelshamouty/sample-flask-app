CREATE USER 'guestbook'@'%' IDENTIFIED BY 'abc123';
GRANT ALL PRIVILEGES ON guestbook.* TO 'guestbook'@'%'; 
