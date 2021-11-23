

class Portfolio:
    def __init__(self):
        self._stocks=[]

    def buy(self,name,shares,price):
        self._stocks.append((name,shares,price))

    def cost(self):
        return sum(
            shares*price for _, shares, price in self._stocks
        )#拆分tuple  _表示不在意这个元素，即name，只需要第二三个元素，即shares and price

