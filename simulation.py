import matplotlib.pyplot as plt

from market import Market
from market_maker import MarketMaker


class Simulation:

    def __init__(self, steps=500):

        self.steps = steps

        self.market = Market()
        self.market_maker = MarketMaker()

        self.market_prices = []
        self.bid_prices = []
        self.ask_prices = []

        self.inventory_history = []
        self.cash_history = []
        self.pnl_history = []

        self.buy_orders = 0
        self.sell_orders = 0
        self.no_trades = 0

    def run(self):

        for _ in range(self.steps):

            # Natural market movement
            self.market.update_price()

            market_price = self.market.get_price()

            # Market maker quotes
            bid, ask = self.market_maker.quote_prices(market_price)

            # Customer order
            order = self.market_maker.generate_order()

            if order == "CUSTOMER_BUY":
                self.buy_orders += 1

            elif order == "CUSTOMER_SELL":
                self.sell_orders += 1

            else:
                self.no_trades += 1

            # Execute trade
            self.market_maker.execute_trade(order, bid, ask)

            # Trade impacts market
            self.market.apply_market_impact(order)

            # Portfolio value
            portfolio = self.market_maker.calculate_portfolio(
                self.market.get_price()
            )

            # Store history
            self.market_prices.append(self.market.get_price())
            self.bid_prices.append(bid)
            self.ask_prices.append(ask)

            self.inventory_history.append(portfolio["inventory"])
            self.cash_history.append(portfolio["cash"])
            self.pnl_history.append(portfolio["pnl"])

    def print_summary(self):

        print("\n========== Simulation Summary ==========\n")

        print(f"Steps                 : {self.steps}")
        print(f"Customer Buy Orders   : {self.buy_orders}")
        print(f"Customer Sell Orders  : {self.sell_orders}")
        print(f"No Trades             : {self.no_trades}")

        print()

        print(f"Final Inventory       : {self.inventory_history[-1]}")
        print(f"Final Cash            : {self.cash_history[-1]:.2f}")
        print(f"Final PnL             : {self.pnl_history[-1]:.2f}")

        print()

        print(f"Maximum PnL           : {max(self.pnl_history):.2f}")
        print(f"Minimum PnL           : {min(self.pnl_history):.2f}")

        print(f"Maximum Inventory     : {max(self.inventory_history)}")
        print(f"Minimum Inventory     : {min(self.inventory_history)}")

    def plot_results(self):

        plt.figure(figsize=(12, 6))

        plt.plot(
            self.market_prices,
            label="Market Price"
        )

        plt.plot(
            self.bid_prices,
            linestyle="--",
            alpha=0.7,
            label="Bid"
        )

        plt.plot(
            self.ask_prices,
            linestyle="--",
            alpha=0.7,
            label="Ask"
        )

        plt.title("Market Price and Quotes")
        plt.xlabel("Time Step")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True)

        plt.show()

        plt.figure(figsize=(12, 4))

        plt.plot(self.inventory_history)

        plt.title("Inventory")
        plt.xlabel("Time Step")
        plt.ylabel("Shares")
        plt.grid(True)

        plt.show()

        plt.figure(figsize=(12, 4))

        plt.plot(self.pnl_history)

        plt.title("Profit and Loss")
        plt.xlabel("Time Step")
        plt.ylabel("PnL")
        plt.grid(True)

        plt.show()


