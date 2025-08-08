from pydantic import BaseModel
from typing import List

class SalesData(BaseModel):
    product_id : str
    date : str
    units_sold : int
    market_trend_index : float
    price : float

class InventoryData(BaseModel):
    product_id : str
    current_stock : int
    warehouse : str