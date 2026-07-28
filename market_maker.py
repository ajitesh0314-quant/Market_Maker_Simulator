import random


class MarketMaker:
    def __init__(
        self,
        spread=0.20,
        initial_cash=10000,
        inventory_sensitivity=0.02,
        base_buy_probability=0.40,
        base_sell_probability=0.40,
        sentiment_strength=0.10
    ):

        self.spread = spread
        self.initial_cash = initial_cash
        self.cash = initial_cash
        self.inventory = 0

        self.inventory_sensitivity = inventory_sensitivity

        self.base_buy_probability = base_buy_probability
        self.base_sell_probability = base_sell_probability
        self.sentiment_strength = sentiment_strength

    def quote_prices(self, market_price):

        inventory_adjustment = (
            self.inventory * self.inventory_sensitivity
        )

        bid = (
            market_price
            - (self.spread / 2)
            - inventory_adjustment
        )

        ask = (
            market_price
            + (self.spread / 2)
            - inventory_adjustment
        )

        return round(bid, 2), round(ask, 2)

    def generate_order(self):

        sentiment = random.uniform(-1, 1)

        buy_probability = (
            self.base_buy_probability
            + self.sentiment_strength * sentiment
        )

        sell_probability = (
            self.base_sell_probability
            - self.sentiment_strength * sentiment
        )

        buy_probability = max(0.10, min(0.80, buy_probability))
        sell_probability = max(0.10, min(0.80, sell_probability))

        event = random.random()

        if event < sell_probability:
            return "CUSTOMER_SELL"

        elif event < sell_probability + buy_probability:
            return "CUSTOMER_BUY"

        return "NONE"

    def execute_trade(self, order, bid, ask):

        if order == "CUSTOMER_SELL":

            self.cash -= bid
            self.inventory += 1

        elif order == "CUSTOMER_BUY":

            if self.inventory > 0:

                self.cash += ask
                self.inventory -= 1

    def calculate_portfolio(self, market_price):

        inventory_value = self.inventory * market_price

        portfolio_value = (
            self.cash + inventory_value
        )

        pnl = portfolio_value - self.initial_cash

        return {
            "inventory": self.inventory,
            "cash": round(self.cash, 2),
            "inventory_value": round(inventory_value, 2),
            "portfolio_value": round(portfolio_value, 2),
            "pnl": round(pnl, 2)
        }

    def reset(self):

        self.cash = self.initial_cash
        self.inventory = 0

