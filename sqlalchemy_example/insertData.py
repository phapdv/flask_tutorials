#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from sqlalchemy import create_engine, insert, Table, MetaData, delete
from app import connection, cookies

# engine = create_engine('sqlite:///example.db')
# metadata = MetaData(engine)
# connection = engine.connect()
# cookies = Table('cookies', metadata, autoload=True)

connection.execute('delete from cookies')
ins = cookies.insert(values=dict(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50"
))
result = connection.execute(ins)
ins = cookies.insert()
result = connection.execute(ins, cookie_name='dark chocolate chip',
                            cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
                            cookie_sku='CC02',
                            quantity='1',
                            unit_cost='0.75')
connection.close()
