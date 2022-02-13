from pydantic import BaseModel, AnyUrl
from typing import Optional
from internal.urls_binance_requests import urls

class DataGetPrice(BaseModel):
    url: AnyUrl = urls["price"]

class BodyGetPriceInterface(BaseModel):
    symbol: Optional[str]

class GetPriceInterface(BaseModel):
    data: DataGetPrice = DataGetPrice()
    body: BodyGetPriceInterface
