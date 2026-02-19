import pandas as pd
from finance.ratios import calculate_ratios


def analyze_financials(file_path: str):
    df = pd.read_csv(file_path)

    df = calculate_ratios(df)

    summary = {
        "latest_year": df.iloc[-1]["Year"],
        "revenue_growth_latest": df.iloc[-1]["Revenue_Growth_%"],
        "ebitda_margin_latest": df.iloc[-1]["EBITDA_Margin_%"],
        "net_margin_latest": df.iloc[-1]["Net_Margin_%"],
        "debt_to_equity_latest": df.iloc[-1]["Debt_to_Equity"],
        "operating_cf_latest": df.iloc[-1]["OperatingCF"]
    }

    return df, summary
