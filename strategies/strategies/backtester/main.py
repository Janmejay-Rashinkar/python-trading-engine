from data.data_loader import load_csv
from strategies.sma_strategy import apply_sma_strategy
from backtester.backtest import backtest

df = load_csv("data/sample_data.csv")
df = apply_sma_strategy(df)

result = backtest(df)
print(f"Final Portfolio Value: {result}")
