import pandas as pd

# loading the data here
df0 = pd.read_csv('data/daily_sales_data_0.csv')
df1 = pd.read_csv('data/daily_sales_data_1.csv')
df2 = pd.read_csv('data/daily_sales_data_2.csv')


# combining them into a single dataframe
df = pd.concat([df0, df1, df2])

# filtering for the pink morsel product
df = df[df['product'] == 'pink morsel']

# cleaning the price column
df['price'] = df['price'].str.replace('$', '').astype(float)

# calculate the sales column
# sales = quantity * price
df['sales'] = df['quantity'] * df['price']

# selecting only the required columns based on the task
out_df = df[['sales', 'date', 'region']]

# saving the output dataframe to a new csv file
out_df.to_csv('data/formatted_data.csv', index=False)

