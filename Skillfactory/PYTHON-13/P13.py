import pandas as pd
orders = pd.read_csv('data/orders.csv', sep = ';')
products = pd.read_csv('data/products.csv', sep = ';')
orders.head()
products.head()
#print(products.columns)
#print(orders.columns)
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
covid_data = pd.read_csv('data/covid_data.csv')
covid_data.head()
#print(covid_data.columns)
vaccinations_data = pd.read_csv('data/country_vaccinations.csv')
vaccinations_data = vaccinations_data[
    ['country', 'date', 'total_vaccinations', 
     'people_vaccinated', 'people_vaccinated_per_hundred',
     'people_fully_vaccinated', 'people_fully_vaccinated_per_hundred',
     'daily_vaccinations', 'vaccines']
]
covid_data = covid_data.groupby(['date','country'], as_index=False)[['confirmed', 'deaths', 'recovered']].sum()
covid_data['date']= pd.to_datetime(covid_data['date'])
covid_data['active']= covid_data['confirmed'] - covid_data['deaths'] - covid_data['recovered']#еще болеют
covid_data = covid_data.sort_values(by= ['country', 'date'])
covid_data['daily_confirmed'] = covid_data.groupby('country')['confirmed'].diff()#прирост заболеваемости
covid_data['daily_deaths'] = covid_data.groupby('country')['deaths'].diff()#прирост смертности
covid_data['daily_recovered'] = covid_data.groupby('country')['recovered'].diff()#прирост выздоровевших
vaccinations_data['date'] = pd.to_datetime(vaccinations_data['date'])
#print(f"Данные о заболеваемости предоставлены от {vaccinations_data['date'].min()} до  {vaccinations_data['date'].max()}")
covid_df = covid_data.merge(vaccinations_data, how='left', on=['date', 'country'])
covid_df['death_rate'] = covid_df['deaths'] /covid_df['confirmed']*100
covid_df['recover_rate'] = covid_df['recovered']/covid_df['confirmed']*100
#print(round(covid_df[covid_df['country'] == 'United States']['death_rate'].max(), 2))
print(round(covid_df[covid_df['country']=='Russia']['recover_rate'].mean(), 2))