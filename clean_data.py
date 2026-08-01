import pandas as pd
import os

# Read Excel file
current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, "Dataset for Data Analytics.xlsx")

df = pd.read_excel(file_path)

# Display column names
print(df.columns.tolist())

# ----------------------------
# Handle Missing Values
# ----------------------------
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# ----------------------------
# Remove Duplicate Rows
# ----------------------------
df = df.drop_duplicates()

# ----------------------------
# Correct Date Format
# ----------------------------
df["Date"] = pd.to_datetime(df["Date"])

# ----------------------------
# Remove Extra Spaces
# ----------------------------
text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].str.strip()

# ----------------------------
# Save Cleaned Dataset
# ----------------------------
df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("\nData Cleaning Completed Successfully!")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)