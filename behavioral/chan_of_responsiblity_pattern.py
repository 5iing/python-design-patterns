# cor_pricing_min_oop.py
from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class PriceRequest:
    base: int
    has_coupon: bool = False
    is_vip: bool = False
    qty: int = 1

class Handler(ABC):
    def __init__(self):
        self._next: Handler | None = None

    def set_next(self, nxt: "Handler") -> "Handler":
        self._next = nxt
        return nxt

    def handle(self, req: PriceRequest) -> int:
        price = self.process(req)
        if price is not None:         
            return price
        if self._next:
            return self._next.handle(req)
        else:
            return req.base

    @abstractmethod
    def process(self, req: PriceRequest) -> int | None: ...

class Coupon(Handler):
    def process(self, req: PriceRequest) -> int | None:
        if req.has_coupon:
            return int(req.base * 0.9)
        else:
            return None

class Loyalty(Handler):
    def process(self, req: PriceRequest) -> int | None:
        if req.is_vip:
            return req.base - 500
        else:
            return None

class Bulk(Handler):
    def process(self, req: PriceRequest) -> int | None:
        if req.qty >= 5:
            return int(req.base * 0.85)
        else:
            return None

def build_chain() -> Handler:
    head = Coupon()
    head.set_next(Loyalty()).set_next(Bulk())
    return head

if __name__ == "__main__":
    chain = build_chain()
    cases = [
        PriceRequest(5000, has_coupon=True),
        PriceRequest(5000, is_vip=True),
        PriceRequest(5000, qty=6),
        PriceRequest(5000),
    ]
    
    for i, req in enumerate(cases, start=1):
        current_request = req
        price = chain.handle(current_request)
        formatted_price = f"{price:,}원" 
        print(f"case {i}, {formatted_price}  {current_request}")