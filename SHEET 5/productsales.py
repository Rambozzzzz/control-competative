n = int(input("Enter number of sales: "))
sales = list(map(int, input("Enter sales: ").split()))[:n]

max_sales = max(sales)
min_sales = min(sales)

print("Max Sales:", max_sales, "Min Sales:", min_sales)
