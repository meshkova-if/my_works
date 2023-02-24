import pandas as pd
melb_data = pd.read_csv('data/melb_data_fe.csv')
melb_data.head()
#print(melb_data.info())
melb_data['Date']= pd.to_datetime(melb_data['Date'])
#print(melb_data.info())
melb_data['Date'] = melb_data['Date'].dt.quarter
#print(melb_data['Date'].value_counts())
#cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car']
#max_unique_count = 150
#for col in melb_data.columns:
    #if melb_data[col].nunique()<max_unique_count and col not in cols_to_exclude:
        #melb_data[col] = melb_data[col].astype('category')
#print(melb_data.info())
#print(melb_data.sort_values(by='Price').head(50))
#print(melb_data.sort_values(by='Date', ascending=False))
#melb_data.sort_values(by='Date', ascending=False)
#print(melb_data.sort_values(by=['Distance', 'Price']).loc[::10, ['Distance', 'Price']])
#mask1 = melb_data['AreaRatio'] < -0.8
#mask2 = melb_data['Type'] == 'townhouse'
#mask3 = melb_data['SellerG'] == 'McGrath'
#print(melb_data[mask1 & mask2 & mask3].sort_values(
    #by=['Date', 'AreaRatio'],
    #ascending=[True, False],
    #ignore_index=True).loc[:, ['Date', 'AreaRatio']])
#print(melb_data.sort_values(by='AreaRatio', ascending=False, ignore_index=True).loc[1558,'BuildingArea'])
#print(melb_data.sort_values())
#mask2 = melb_data['Rooms'] > 2
#mask1 = melb_data['Type'] == 'townhouse' 
#print(int(melb_data[mask1 & mask2].sort_values(by=['Rooms', 'MeanRoomsSquare'], ascending=[True, False], ignore_index=True).loc[18, 'Price']))
#print(melb_data.groupby(by='Type', as_index=False).mean())
#print(melb_data.groupby(by='Type') ['Price'].sum())
#print(melb_data.groupby('Regionname')['Distance'].min().sort_values(ascending=False))
#print(melb_data.groupby('MonthSale')['Price'].agg(['count', 'mean', 'max']).sort_values(by='MonthSale', ascending=True))
#print(melb_data.groupby('Regionname')['SellerG'].agg(['nunique', set]))
#print(melb_data.groupby('Rooms')['Price'].mean().sort_values(ascending=False))
#print(melb_data.groupby('Regionname')['Lattitude'].std().sort_values(ascending=False))
#print(melb_data.info())
#print(melb_data.groupby('Rooms')[['Rooms']].median())
#print(melb_data.groupby(['Rooms', 'Type'])['Price'].mean().unstack())
#print(melb_data.pivot_table(values='Price', index='Rooms', columns='Type', fill_value=0).round())
#print(melb_data.pivot_table(values='Price', index='Regionname', columns='Weekend', aggfunc='count'))
#print (melb_data.pivot_table(values='Landsize', index= 'Regionname', columns= 'Type', aggfunc=['mean', 'median'], fill_value=0))
#print(melb_data.pivot_table(values='Price', index= ['Method','Type'], columns='Regionname', aggfunc='median', fill_value=0))
#pivot = melb_data.pivot_table(values='Landsize', index= 'Regionname', columns= 'Type', aggfunc=['mean', 'median'], fill_value=0)
#print(pivot.columns)
#print(pivot['mean']['unit'])
#mask = pivot['mean']['house']<pivot['median']['house']
#filter_pivot = pivot[mask]
#print(filter_pivot)
BuildingArea = melb_data.pivot_table(values='BuildingArea', index='Type',columns='Rooms',  aggfunc=['median'], fill_value=0)
#print(BuildingArea)
SellerG = melb_data.pivot_table(values='Price', index='SellerG',columns='Type', aggfunc=['median'], fill_value=0 )
#print(SellerG['median']['unit'])
dates = pd.read_csv('data/dates.csv')
movies = pd.read_csv('data/movies.csv')
ratings1 = pd.read_csv('data/ratings1.csv')
ratings2 = pd.read_csv('data/ratings2.csv')
ratings = pd.concat([ratings1, ratings2], ignore_index=True)
ratings = ratings.drop_duplicates(ignore_index=True)
#print(ratings.shape[0])
#print(dates.shape[0])
ratings_dates = pd.concat([ratings, dates], axis=1)
#print(ratings_dates.tail(7))
#joined_false= ratings_dates.join(movies, how='outer', lsuffix ='_right')
#print(joined_false)
merged=ratings_dates.merge(movies, on='movieId', how='left') 
#print(merged)
#print('Число строк в ratings_date:',ratings_dates.shape[0])
#print('Число строк в merged:', merged.shape[0])
#print(ratings_dates.shape[0] == merged.shape[0])
merged2= ratings_dates.merge(movies, on = 'movieId',how='outer')
#print(merged2.shape[0])
a = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [103, 214, 124], 'C': [1, 4, 2]})
#print(a)
items_df = pd.DataFrame({
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394], 
    'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],
    'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]
})
purchase_df = pd.DataFrame({
    'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132], 
    'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]
})
merged3= items_df.merge(purchase_df, on = 'item_id', how = 'inner')
income =(merged3['price']*items_df['stock_count']).sum()
#print(income)
joined = pd.read_csv('data/ratings_movies.csv')
#print(ratings_movies)
joined['date']= pd.to_datetime(joined['date'], dayfirst=True)
import re 
def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg) 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None
#print(ratings_movies.info())
#print(ratings_movies['date'].value_counts())
#year_release  = ratings_movies['date'].dt.year
#print(year_release.info(None))
#joined['year_release'] = joined['title'].apply(get_year_release)
#print(joined.info())
#print(joined['year_release']['rating']['genres'])#наименьшая средняя оценка
#genres 2010 году получило наименьшую среднюю оценку (rating)
#mask = joined['year_release'] == 2010
#print(joined[mask].groupby('genres')['rating'].mean().sort_values())
#userId уникальных комбинаций жанров (genres) фильмов
#print(joined.groupby('userId')['genres'].nunique().sort_values(ascending=False))
#Сгруппируйте таблицу по пользователям и найдите число уникальных жанров для каждого пользователя.
#Отсортируйте результат по убыванию.
#Индекс первой строки результирующей таблицы будет являться ответом.
#print(joined.groupby('userId')['rating'].agg(['count', 'mean']).sort_values(by=['count','mean'], ascending=[False, True]))
#Найдите пользователя, который выставил наименьшее количество оценок, но его средняя оценка фильмам наибольшая.
#mask = joined['year_release'] == 2018
#mask_group = joined[mask].groupby('genres')['rating'].agg(['count', 'mean']).sort_values(by=['count','mean'], ascending=False)
#print(mask_group[mask_group['count']>10].sort_values(
    #by='mean',
    #ascending=False))
#joined['year_rating'] = joined['date'].dt.year
#print(joined['year_rating'])
#svod = joined.pivot_table(values='rating', index='year_rating', columns='genres', aggfunc='mean')
#print(svod['Animation|Children|Mystery'])
#date1 = joined['date'] ==[2017]
#date2 = joined['date'] ==[2018]
#mask = (date1 <= melb_data['Date']) & (melb_data['Date'] <= date2)
#print(melb_data[mask].groupby('SellerG')['Price'].sum().sort_values(ascending=True))
#joined['date']= pd.to_datetime(joined['date'], dayfirst=True)
#joined['dates']= joined['date'].dt.date

#print(melb_data.columns)
melb_data['Date']= pd.to_datetime(melb_data['Date'])
date1 = pd.to_datetime('2017-05-01') 
date2 = pd.to_datetime('2017-09-01')
#mask = (date1 <= melb_data['Date']) & (melb_data['Date'] <= date2)
mask = (melb_data['Date']>='2017-05-01')&(melb_data['Date']<='2017-09-01')
n = melb_data[mask].groupby('SellerG')['Price'].sum().sort_values(ascending=True)
#print(n)






