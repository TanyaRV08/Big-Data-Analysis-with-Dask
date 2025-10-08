# Overseas Trade Indexes Analysis (June 2025 Quarter)

This project analyzes New Zealand's *Overseas Trade Indexes (June 2025 Quarter, Provisional)* dataset using **Dask** and **Pandas** for efficient large-scale data processing.

---

## Overview

The script performs the following:

1. Loads the large CSV dataset using **Dask**.
2. Checks data partitions and missing values.
3. Converts numeric and date-like columns into appropriate types.
4. Generates descriptive statistics for trade data.
5. Identifies the **Top 10 trade series** based on average Data Value.
6. Extracts **trend insights** for the top 5 series across years.
7. Exports results to CSV files for further visualization or reporting.

---

## Technologies Used

* **Python 3.10+**
* **Dask** – for parallel and scalable data processing
* **Pandas** – for data manipulation and summary statistics
* **Time** – to measure execution duration

---

## File Structure

```
├── Task 1.py                     # Main analysis script
├── overseas-trade-indexes-june-2025-quarter-provisional.csv  # Input dataset
├── output_dask_top_series.csv    # Output: Top 10 series summary
└── output_dask_trend.csv         # Output: Trend analysis for top 5 series
```

---

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
2. Install required packages:

   ```bash
   pip install dask pandas
   ```
3. Update the file paths in `Task 1.py` to match your local setup:

   ```python
   file_path = r"path_to_your_dataset.csv"
   output_path = r"path_to_save_outputs"
   ```
4. Run the script:

   ```bash
   python Task\ 1.py
   ```

---

## Outputs

* **Top Series Summary:** Lists the top 10 series by average Data Value.
* **Trend Analysis:** Year-wise average Data Values for the top 5 series.
* Execution time summary displayed in console.

---

## Insights

This analysis provides a quick overview of trade performance trends and identifies leading series in terms of data value growth or consistency.

---

## Author

**Tanya V**
Internship Project — Data Analysis using Dask
 *October 2025*

---

## License
This project is for educational and research purposes.
Dataset © Stats NZ | Code © Tanya V, 2025

