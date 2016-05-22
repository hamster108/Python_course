select * from Users;
select COUNT(id) from Users;
select COUNT(id) from Users WHERE birth_date <= date('1976-05-11');
select country, count(country) from Users group by country;
select name, count(name) from Users group by name having count(*)>1;
select count(id) from Orders where created >= date('2016-01-01');
select date(created), count(date(created)) from Orders group by date(created) order by count(*) desc limit 1;
select (select count(paid)*100 from Orders where paid is 0)/count(id) from Orders;
select * from Goods where name like '%bread%';

select (select id from Goods where id in (select good_id from GoodsInOrders where good_id group by good_id order by count(good_id) desc limit 10)), name, quantity from Goods limit 10;

select sum(g.price) as summa from Goods g inner join GoodsInOrders go on g.id=go.good_id where g.id in (select go.good_id from GoodsInOrders go inner join Orders o on go.order_id=o.id where o.id in (select id from Orders where paid=1 and date(created)>= date('2016-01-01')));

select name from Goods g inner join GoodsInOrders go on g.id=go.good_id where go.good_id in (select o.id from Orders o inner join Users u on o.user_id=u.id where u.id in (select id from Users where gender='F')) and go.good_id group by go.good_id order by count(go.good_id) desc limit 10;

select name from Users u inner join Orders o on u.id=o.user_id where o.user_id in (select o.user_id from Orders o inner join GoodsInOrders go on o.id=go.order_id where go.order_id in (select go.order_id from GoodsInOrders go inner join Goods g on go.good_id=g.id where g.id in (select id from Goods g where g.units='KG' and g.quantity order by g.quantity desc))) limit 1;











