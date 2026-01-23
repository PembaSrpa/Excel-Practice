import pandas as pd
import numpy as np
from datetime import datetime, timedelta

n_rows = 1000

# Lists for variety
regions = ["Sub-Saharan Africa", "Europe", "Asia", "North America", "Central America and the Caribbean", "Middle East and North Africa", "Australia and Oceania"]
countries = ["Nepal", "Namibia", "Germany", "USA", "Canada", "United Kingdom", "Japan", "Australia", "India", "South Africa", "Brazil", "Mexico"]
reps = ["Suman K.", "John Doe", "Jane Smith", "Emily Davis", "Liam Wilson", "Sarah Chen", "Arjun P.", "Maria G."]
item_types = ["Household", "Beverages", "Office Supplies", "Meat", "Snacks", "Vegetables", "Fruits", "Personal Care", "Clothes", "Cosmetics", "Cereal", "Baby Food"]

np.random.seed(42)

data = {
    "Region": np.random.choice(regions, n_rows),
    "Country": np.random.choice(countries, n_rows), # Fixed
    "Item Type": np.random.choice(item_types, n_rows),
    "Rep Name": np.random.choice(reps, n_rows),     # Fixed
    "Sales Channel": np.random.choice(["Online", "Offline"], n_rows),
    "Order Priority": np.random.choice(["H", "L", "M", "C"], n_rows),
    "Units Sold": np.random.randint(10, 5000, n_rows),
    "Unit Price": np.round(np.random.uniform(20, 500, n_rows), 2),
    "Unit Cost": np.round(np.random.uniform(10, 300, n_rows), 2)
}

# Date Logic
start_date = datetime(2024, 1, 1)
data["Order Date"] = [start_date + timedelta(days=np.random.randint(0, 730)) for _ in range(n_rows)]
data["Order Id"] = np.random.randint(100000000, 999999999, n_rows)
data["Ship Date"] = [d + timedelta(days=np.random.randint(1, 14)) for d in data["Order Date"]]

df = pd.DataFrame(data)

# Calculated Columns
df["Total Revenue"] = df["Units Sold"] * df["Unit Price"]
df["Total Cost"] = df["Units Sold"] * df["Unit Cost"]
df["Total Profit"] = df["Total Revenue"] - df["Total Cost"]
df["Order_Year"] = df["Order Date"].dt.year
df["Order_Month"] = df["Order Date"].dt.strftime("%B")

# Formatting for CSV
df["Order Date"] = df["Order Date"].dt.strftime("%Y-%m-%d")
df["Ship Date"] = df["Ship Date"].dt.strftime("%Y-%m-%d")

# Column Order
cols = ["Region", "Country", "Item Type", "Rep Name", "Sales Channel", "Order Priority", "Order Date", "Order Id", "Ship Date", "Units Sold", "Unit Price", "Unit Cost", "Total Revenue", "Total Cost", "Total Profit", "Order_Year", "Order_Month"]
df = df[cols]

df.to_csv("sales_data.csv", index=False)
