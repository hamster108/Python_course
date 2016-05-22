import sqlite3 as sq


def unpaid(user_id):
    with sq.connect("/home/elizaveta/Downloads/last_homework/data.sqlite") as con:
        cur = con.cursor()
    query = ("select u.name, o.id, sum(g.price) from Users u inner join Orders o on u.id=o.user_id "
            "inner join GoodsInOrders go on o.id=go.order_id "
            "inner join Goods g on go.good_id=g.id "
            "where u.id=? and o.paid = 0 group by o.id")
    data = cur.execute(query , [user_id]). fetchall()
    return data


print(unpaid (23))

