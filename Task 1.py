import dask.dataframe as dd
import pandas as pd
import time

file_path = r"C:\Users\khali\OneDrive\Desktop\Tanya Intern\overseas-trade-indexes-june-2025-quarter-provisional.csv"

start = time.time()
df = dd.read_csv(file_path, dtype=str, assume_missing=True)
print("Initial partitions:", df.npartitions)

row_count = len(df)
print("Row count:", row_count)

df["Data_value"] = dd.to_numeric(df["Data_value"], errors="coerce").astype("float64")
df["Year"] = df["Period"].astype(str).str.split(".").str[0]

missing_counts = df.isna().sum().compute()
print("\nMissing values per column:\n", missing_counts)

stats = df["Data_value"].astype("float64").describe().compute()
print("\nData_value stats:\n", stats)

series_cols = [c for c in df.columns if "Series_title" in c]
target_col = series_cols[-1] if series_cols else "Subject"

top_series = (
    df.groupby(target_col)["Data_value"]
    .mean()
    .nlargest(10)
    .compute()
)
print("\nTop 10 series by average Data_value:\n", top_series)

top5_names = top_series.index[:5].tolist()
trend = (
    df[df[target_col].isin(top5_names)]
    .groupby(["Year", target_col])["Data_value"]
    .mean()
    .compute()
    .reset_index()
)
print("\nTrend sample for top 5 series:\n", trend.head(20))

output_path = r"C:\Users\khali\OneDrive\Desktop\Tanya Intern\output_dask"
top_series.to_csv(output_path + "_top_series.csv")
trend.to_csv(output_path + "_trend.csv", index=False)

print("\nAnalysis completed in", round(time.time() - start, 2), "seconds")
