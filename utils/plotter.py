from data.data_loader import load_csv
from strategies.sma_strategy import apply_sma_strategy
from backtester.backtest import backtest
from utils.performance import calculate_returns
from utils.plotter import plot_equity_curve

df = load_csv("data/sample_data.csv")
df = apply_sma_strategy(df)

final_value = backtest(df)
metrics = calculate_returns(df)

print(f"Final Portfolio Value: {final_value}")
print(f"Total Return: {metrics['total_return']}%")
print(f"Volatility: {metrics['volatility']}%")

plot_equity_curve(df)
