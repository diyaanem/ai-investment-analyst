import pandas as pd


def calculate_ratios(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute financial ratios.
    """

    df["Revenue_Growth_%"] = df["Revenue"].pct_change() * 100
    df["EBITDA_Margin_%"] = (df["EBITDA"] / df["Revenue"]) * 100
    df["Net_Margin_%"] = (df["NetProfit"] / df["Revenue"]) * 100
    df["Debt_to_Equity"] = df["Debt"] / df["Equity"]

    return df
