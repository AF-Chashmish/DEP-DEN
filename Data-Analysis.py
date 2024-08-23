import pandas as pd
import matplotlib.pyplot as plt
file_path = r"E:\VS CODE\Internship Python\Task 3\SaleData.xlsx"
df = pd.read_excel(file_path)
sales = pd.read_excel("E:\VS CODE\Internship Python\Task 3\SaleData.xlsx")

print(df.tail())
print(df.describe())
print(df.info())
print(df.isnull().sum())

sales['year'] = sales['OrderDate'].dt.year
sales['month'] = sales['OrderDate'].dt.month
sales['Region'] = sales['Region'].astype('category')
sales['Item'] = sales['Item'].astype('category')

plt.figure(figsize=(8, 6))
plt.bar(sales['Region'].cat.categories, sales.groupby('Region')['Sale_amt'].sum(), alpha=0.7, color='yellow', edgecolor='purple')
plt.title('Total Sales by Regions')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(sales.groupby('month')['Sale_amt'].sum(), marker='v', linestyle='-')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

top_products = sales.groupby('Item')['Sale_amt'].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(8, 6))
plt.bar(top_products.index, top_products.values, alpha=0.7, color='blue', edgecolor='red')
plt.title('Top 5 Items by Sales')
plt.xlabel('Item')
plt.ylabel('Total Sales')
plt.show()

sales_pivot = sales.pivot_table(index='Region', columns='Item', values='Sale_amt', aggfunc='sum', observed=False)
plt.figure(figsize=(10, 8))
plt.imshow(sales_pivot, cmap='coolwarm', interpolation='nearest')
plt.title('Sales by Regions and Items')
plt.xlabel('Item')
plt.ylabel('Region')
plt.colorbar()
plt.show()
