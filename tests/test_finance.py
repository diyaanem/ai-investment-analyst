from finance.analyzer import analyze_financials

df, summary = analyze_financials("data/raw/financials.csv")

print("\nFULL DATAFRAME:\n")
print(df)

print("\nSUMMARY:\n")
print(summary)
