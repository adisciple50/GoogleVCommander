__author__ = 'deddo_000'
import mysql



connection = mysql.connect("127.0.0.1","ThisPassword")
connection.selectdb("Groceries")


FruitsArray = mysql.Query("FROM GreenGrocers Select Fruits")
FruitsArray.Execute()