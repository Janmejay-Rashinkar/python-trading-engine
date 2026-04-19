import pandas as pd


def calculate_returns(df: pd.DataFrame):
    df["returns"] = df["close"].pct_change()
    total_return = (df["close"].iloc[-1] / df["close"].iloc[0]) - 1
    volatility = df["returns"].std() * (252 ** 0.5)

    return {
        "total_return": round(total_return * 100, 2),
        "volatility": round(volatility * 100, 2),
    }
