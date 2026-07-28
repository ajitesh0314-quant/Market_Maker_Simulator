import random


class Market:
    def __init__(
        self,
        initial_price=100.0,
        volatility=0.30,
        market_impact=0.05
    ):
        self.price = initial_price
        self.volatility = volatility
        self.market_impact = market_impact

    def update_price(self):
        """
        Simulate natural market movement using a Gaussian random walk.
        """
        self.price += random.gauss(0, self.volatility)

        # Prevent unrealistic negative prices
        self.price = max(1.0, self.price)

        self.price = round(self.price, 2)

        return self.price

    def apply_market_impact(self, order):

        if order == "CUSTOMER_BUY":
            self.price += self.market_impact

        elif order == "CUSTOMER_SELL":
            self.price -= self.market_impact

        self.price = max(1.0, self.price)
        self.price = round(self.price, 2)

        return self.price

    def get_price(self):
        return self.price

    def reset(self, initial_price=100.0):
        self.price = initial_price