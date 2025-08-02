'''author:Savio Bijo Thomas
   date=19-11-24
   purpose=Inventory management system using tuple'''

inventory=[
 ("laptop",5,30000),
 ("headphones",15,500),
 ("mouse",50,200),
 ("keyboard",30,500)
 ]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name,quantity,unit_price=item
    stock_value=quantity*unit_price
    print("item name",item_name,"stock value is",stock_value)
    if stock_value>highest_stock_value:
        stock_value=highest_stock_value
        item_with_highest_stock_value=item_name
print("highest stock value is",highest_stock_value)
print("item with highest stock value is",item_with_highest_stock_value)
