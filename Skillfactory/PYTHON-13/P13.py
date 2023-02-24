import pandas as pd
orders = pd.read_csv('data/orders.csv', sep = ';')
products = pd.read_csv('data/products.csv', sep = ';')
orders.head()
products.head()
#print(products.columns)
print(orders.columns)
#m = orders.merge(products, how='inner', on=)
orders_products = orders.merge(
    products, 
    left_on='ID товара',
    right_on='Product_ID',
    how='left')
orders_products['Дата создания'] = pd.to_datetime(orders_products['Дата создания'])
#print(orders_products[orders_products['Name'].isna()])
#print(orders_products[orders_products['Статус']=='Отменён'])
orders_products['col_pr'] = (orders_products['Количество']*orders_products['Price'])
#&(orders_products['Оплачен'] == 'Да')
#print(orders_products[orders_products['Оплачен'] == 'Да'].groupby('ID Покупателя')['col_pr'].sum().sort_values(ascending=False))

