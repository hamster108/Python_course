select username from Users order by username;

select username from Users order by date(registered) desc limit 5;

select u.username, count(*) from Listened l inner join Users u on u.id =l.user_id group by user_id order by count(*) desc limit 5;

select a.id, count(*) from Artists a inner join Albums al on a.id=al.artist_id group by a.id;

select a.id, count(s.id) from Artists a inner join Albums al on a.id=al.artist_id inner join Songs s on al.id=s.album_id group by a.id;

select a.name, al.name, count(s.id) from Artists a inner join Albums al on a.id=al.artist_id inner join Songs s on al.id=s.album_id group by s.album_id order by count(s.id) desc limit 1;

select a.name, al.name, sum(s.duration) from Artists a inner join Albums al on a.id=al.artist_id inner join Songs s on al.id=s.album_id group by s.album_id order by sum(s.duration) desc limit 1;

select a.name, al.name, avg(s.duration) from Artists a inner join Albums al on a.id=al.artist_id inner join Songs s on al.id=s.album_id group by s.album_id order by avg(s.duration) desc limit 1;

select a.name, al.name, s.name, count(l.song_id) from Artists a inner join Albums al on a.id=al.artist_id inner join Songs s on al.id=s.album_id inner join Listened l on s.id=l.song_id group by s.id order by count(l.song_id) desc limit 5;

select al.release_year, count(*) from Users u inner join Listened l  on u.id = l.user_id inner join Songs s on l.song_id = s.id inner join Albums al on al.id = s.album_id group by al.release_year order by count(*) desc limit 1;

select a.name, al.name, s.name, l.start_time from Listened l inner join Songs s on l.song_id = s.id inner join Albums al on al.id = s.album_id inner join Artists a on a.id = al.artist_id where l.user_id = 47 order by l.start_time desc limit 20;


select u.username, a.name, al.name, s.name, count(*) from Listened l inner join Songs s on  l.song_id = s.id inner join Albums al on al.id = s.album_id inner join Artists a on a.id = al.artist_id inner join Users u on u.id = l.user_id group by l.user_id, l.song_id;



