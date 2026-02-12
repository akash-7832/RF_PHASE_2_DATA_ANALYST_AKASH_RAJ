import pandas as pd

df = pd.read_csv(r"C:\Users\Akash\OneDrive\Documents\OJT\Chocolate Sales (2).csv")
df.head()

df.info()
df.describe()

df.isnull().sum()
df = df.dropna(subset=['Amount'])
df['Country'] = df['Country'].fillna('Unknown')
df.duplicated().sum()
df = df.drop_duplicates()
df.shape

# 1. Which country contributes the highest revenue?
country_sales = (
    df.groupby('Country')['Amount']
    .sum()
    .sort_values(ascending=False)
)


# 2. Which product is the most sold?
product_sales = (
    df.groupby('Product')['Amount']
    .sum()
    .sort_values(ascending=False)
)   

# Fix Date column (DD-MM-YYYY format)
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Clean Amount column (remove $ and , then convert to float)
df['Amount'] = (
    df['Amount']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)

# 3.How does sales performance vary monthly?
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

monthly_sales = df.groupby(['Year', 'Month'])['Amount'].sum().reset_index()


# 4.Top 5 products by revenue
top_products = (
    df.groupby('Product')['Amount']
    .sum()
    .nlargest(5)
)


# 5.Which countries/products underperform?
low_performance = (
    df.groupby('Country')['Amount']
    .sum()
    .nsmallest(3)
)

print(country_sales.head())
print(top_products)

# Save cleaned data 
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

df.to_csv("cleaned_chocolate_sales.csv", index=False)


