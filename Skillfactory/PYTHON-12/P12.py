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
pivot = melb_data.pivot_table(values='Landsize', index= 'Regionname', columns= 'Type', aggfunc=['mean', 'median'], fill_value=0)
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
print(ratings_dates.tail(7))

