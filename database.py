from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")  # ✅


db = client.supply_chain_db # database
sales_collection = db.sales_data #collection
inventory_collection = db.inventory_data #collection