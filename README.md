# Inventory-Aware Market Making Simulator

A Python-based simulation of a market maker operating in a simplified financial market. The project models bid-ask quoting, customer order flow, inventory management, market impact, and portfolio valuation while tracking the profitability of the market maker over time.

---

## Overview

Market makers continuously provide liquidity by quoting both bid and ask prices. They profit from capturing the bid-ask spread while managing the risk of accumulating excessive inventory.

This simulator demonstrates the core mechanics of market making by simulating:

- Random market price movement
- Dynamic bid and ask quotes
- Customer buy and sell orders
- Inventory-aware pricing
- Market impact after each trade
- Portfolio valuation and Profit & Loss (PnL)

---

## Features

- Gaussian random walk market simulation
- Inventory-aware bid and ask pricing
- Configurable bid-ask spread
- Customer order generation with market sentiment
- Market impact from executed trades
- Cash and inventory tracking
- Mark-to-market portfolio valuation
- Performance summary
- Visualization of:
  - Market Price
  - Bid & Ask Quotes
  - Inventory
  - Profit & Loss

---

## Project Structure

```
market-making-simulator/
│
├── market.py
├── market_maker.py
├── simulation.py
├── main.py
├── requirements.txt
├── README.md
└── images/
```

---

## Simulation Workflow

```
                Market
                   │
      Random Price Movement
                   │
                   ▼
          Market Maker Quotes
           (Bid / Ask Prices)
                   │
                   ▼
        Customer Order Generation
                   │
                   ▼
           Trade Execution
                   │
                   ▼
          Market Impact Applied
                   │
                   ▼
     Portfolio & PnL Calculation
                   │
                   ▼
      Statistics & Visualization
```

---

## Technologies Used

- Python 3
- Matplotlib

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/market-making-simulator.git

cd market-making-simulator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the simulator:

```bash
python main.py
```

---

## Sample Output

The simulator produces:

- Market price with bid and ask quotes
- Inventory over time
- Profit and Loss (PnL)
- Simulation summary including:
  - Customer buy orders
  - Customer sell orders
  - Final inventory
  - Final cash
  - Final PnL
  - Maximum and minimum PnL

---

## Example Summary

```
========== Simulation Summary ==========

Steps                 : 500
Customer Buy Orders   : 210
Customer Sell Orders  : 186
No Trades             : 104

Final Inventory       : 16
Final Cash            : 8598.14
Final PnL             : 14.14

Maximum PnL           : 26.00
Minimum PnL           : -3.71
Maximum Inventory     : 16
Minimum Inventory     : 0
```

---

## Key Concepts Demonstrated

- Market Making
- Bid-Ask Spread
- Liquidity Provision
- Inventory Risk Management
- Market Impact
- Mark-to-Market Valuation
- Random Walk Price Simulation
- Object-Oriented Programming in Python

---

## Future Improvements

Possible extensions include:

- Limit Order Book simulation
- Variable order sizes
- Dynamic spread adjustment
- Volatility-dependent quoting
- Transaction costs and exchange fees
- Multi-asset market making
- Performance metrics such as Sharpe Ratio and Maximum Drawdown

---

## Author

**Ajitesh Banda**

Mechanical Engineering Undergraduate  
National Institute of Technology Hamirpur

Interested in Quantitative Trading, Market Microstructure, and Algorithmic Trading.
