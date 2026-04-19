def backtest(df, initial_capital=100000):
    position = 0
    cash = initial_capital

    for _, row in df.iterrows():
        if row["signal"] == 1 and position == 0:
            position = cash / row["close"]
            cash = 0
        elif row["signal"] == -1 and position > 0:
            cash = position * row["close"]
            position = 0

    final_value = cash if position == 0 else position * df.iloc[-1]["close"]
    return final_value
