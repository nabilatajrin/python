# Group by type; calc total weekly sales
sales_by_type = sales['weekly_sales'].groupby(sales["type"]).sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sales_by_type.sum()
print(sales_propn_by_type)

# From previous step
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)
