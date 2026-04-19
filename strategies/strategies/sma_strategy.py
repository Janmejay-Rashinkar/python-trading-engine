import pandas as pd


def apply_sma_strategy(df: pd.DataFrame, short_window=20, long_window=50):
    df["sma_short"] = df["close"].rolling(window=short_window).mean()
    df["sma_long"] = df["close"].rolling(window=long_window).mean()

    df["signal"] = 0
    df.loc[df["sma_short"] > df["sma_long"], "signal"] = 1
    df.loc[df["sma_short"] < df["sma_long"], "signal"] = -1

    return df
