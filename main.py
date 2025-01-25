# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a mock dataset
data = {
    'Order Date': [
        '2023-01-15', '2023-02-20', '2023-03-05', '2023-01-18', '2023-02-25',
        '2023-03-12', '2023-01-10', '2023-02-15', '2023-03-20', '2023-01-25',
        '2023-02-28', '2023-03-30'
    ],
    'Region': ['East', 'West', 'East', 'South', 'West', 'East', 'North', 'South', 'West', 'North', 'South', 'East'],
    'Sub-Category': ['Furniture', 'Technology', 'Furniture', 'Office Supplies', 'Technology', 'Office Supplies',
                     'Furniture', 'Technology', 'Office Supplies', 'Furniture', 'Technology', 'Furniture'],
    'Sales': [230, 450, 300, 200, 600, 150, 400, 500, 350, 250, 700, 450]
}

# Convert to a DataFrame
df = pd.DataFrame(data)

# Convert 'Order Date' to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Add Year and Month columns
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

# 1. Monthly Sales Trends
monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_sales, x='Month', y='Sales', marker='o', color='b')
plt.title("Monthly Sales Trends")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# 2. Top-Performing Regions and Products
top_regions = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print("Top Regions by Sales:\n", top_regions)

top_products = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(10)
print("Top Products by Sales:\n", top_products)

plt.figure(figsize=(10, 6))
top_products.plot(kind='bar', color='orange')
plt.title("Top Products by Sales")
plt.xlabel("Product Sub-Category")
plt.ylabel("Sales")
plt.show()

# 3. Year-over-Year Growth
yearly_sales = df.groupby('Year')['Sales'].sum()
print("Yearly Sales:\n", yearly_sales)

# Calculate YoY growth (mock data has only 1 year, so add a note)
if yearly_sales.size > 1:
    yoy_growth = yearly_sales.pct_change().dropna() * 100
    print("Year-over-Year Growth (%):\n", yoy_growth)
else:
    print("Insufficient years of data to calculate YoY growth.")

# Visualization of Yearly Sales
plt.figure(figsize=(8, 5))
yearly_sales.plot(kind='bar', color='green')
plt.title("Yearly Sales")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()
