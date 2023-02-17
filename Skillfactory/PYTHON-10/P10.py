import pandas as pd
#def create_medications(names, counts):
    #medications = pd.Series(index=names, data=counts)
    #return medications
#def get_percent(medications, name):
    #return(medications.loc[name]/sum(medications) * 100)
#names=['chlorhexidine', 'cyntomycin', 'afobazol']
#counts=[15, 18, 7]
#print(create_medications(names = ['chlorhexidine', 'cyntomycin', 'afobazol'], counts = [26, 18, 7]))
#def create_companyDF(income, expenses, years):
    #df = pd.DataFrame({
        #'Income': income,
        #'Expenses': expenses
        #},
        #index = years
    #)
    #return df
#incomes = [478, 512, 196]
#expenses = [156, 130, 270]
#years = [2018, 2019, 2020]

#def get_profit(df, year):
    #if year in df.index:
        #profit = df.loc[year, 'incomes']-df.loc[year,'expenses']
    #else:
        #profit=None
        #return profit


#print(get_profit(df=incomes,expenses,years))
melb_data = pd.read_csv('data/melb_data.csv', sep=',')
#print(round(melb_data['Landsize'].loc[3521]/melb_data['Landsize'].loc[1690]))
#print(melb_data.info)
#melb_data['Car'] = melb_data['Car'].astype('int64')
#melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
#melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
#melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
#melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')
#print(melb_data.describe().loc[:, ['Distance', 'BuildingArea' , 'Price']])
#data = pd.DataFrame([[0,1], [1, 0], [1, 1]], columns=['А', 'B'])
#print(melb_data.describe(include=['object']))
#print(melb_data['Type'].value_counts(normalize=True))
#print(melb_data['Car'].max())
#rate = 0.12
#income = melb_data['Price'].sum()*rate
#print('Total income of real estate agencies:',round(income,2))
#print(melb_data['Propertycount'].max())
#print(round(melb_data['Distance'].std()))
#building_median = melb_data['BuildingArea'].median() 
#building_mean =  melb_data['BuildingArea'].mean()
#deviance = abs(building_median - building_mean)/building_mean
#print(round(deviance * 100, 2))
#df= pd.DataFrame([1, 2, 4, 2, 3, 2, 1, 5, 6])
#print(df.mode())
#print(melb_data['Bedroom'].mode())
#mask = melb_data['Price'] > 2000000
#print(mask)
#print(melb_data[mask].head())
#print(melb_data[melb_data['Rooms'] == 3].shape[0])
#print(melb_data[(melb_data['Rooms'] == 3) & (melb_data['Price'] < 300000)].shape[0])
#print(melb_data[melb_data['Bathroom'] == 0].shape[0])
#print(melb_data[(melb_data['SellerG'] == 'Nelson') & (melb_data['Price'] > 3e6)].shape[0])
#print(melb_data[(melb_data['BuildingArea'] == 0)]['Price'].min())
#print(round(melb_data[(melb_data['Price']<1e6) & ((melb_data['Rooms']>5) | (melb_data['YearBuilt'] > 2015))]['Price'].mean()))
#print(melb_data[(melb_data['Type'] == 'h') & (melb_data['Price'] < 3000000)]['Regionname'].mode())
#print(melb_data.head())
melb_df= melb_data.copy()
melb_df.head()
melb_df = melb_df.drop(['index', 'Coordinates'], axis=1)
melb_df.head()
#print(melb_df)
total_rooms = melb_df['Rooms']+melb_df['Bedroom']+melb_df['Bathroom']
#print(total_rooms)
melb_df['MeanRoomsSquare'] = melb_df['BuildingArea']/total_rooms
#print(melb_df['MeanRoomsSquare'])
diff_area = melb_df['BuildingArea'] - melb_df['Landsize']
sum_area = melb_df['BuildingArea'] + melb_df['Landsize']
melb_df['AreaRatio'] = diff_area/sum_area
#print(melb_df['AreaRatio'])
#price_square = melb_df['Price'] **2
#print(price_square)
melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
#print(melb_df['Date'])
years_sold = melb_df['Date'].dt.year
#print(years_sold)
#print(years_sold.min())
#print(years_sold.max())
#print(years_sold.mode()[0])
melb_df['MonthSale'] = melb_df['Date'].dt.month
#print(melb_df['MonthSale'].value_counts(normalize=True)*1e6)
#delta_day = melb_df['Date'] - pd.to_datetime('2016-01-01')
#print(delta_day.dt.days)
#melb_df['AgeBuilding'] = melb_df['Date'].dt.year - melb_df['YearBuilt']
#print(melb_df['AgeBuilding'])
#melb_df = melb_df.drop('YearBuilt', axis=1)
melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek
weekend_count = melb_df[(melb_df['WeekdaySale'] == 5) + (melb_df['WeekdaySale'] == 6)].shape[0]
#print(weekend_count)
#NLO = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv', sep = ',')
#print(NLO) 
#NLO['Time'] = pd.to_datetime(NLO.Time)
#print(NLO['Time'].dt.year.mode()[0])
#NLO['Year'] = NLO['Time'].dt.year
#print(NLO['Year'].mode())
#NLO['date'] = NLO['Time'].dt.date
#print(NLO['date'])
#m = NLO[NLO['State']=='NV']['date'].diff().dt.days.mean()
#print(melb_df['Address'].nunique())
#print(melb_df['Address'].loc[177])
#print(melb_df['Address'].loc[1812])
#print(melb_df['Address'].loc[9001])
#def get_street_type(address):
    #exclude_list = ['N', 'S', 'W', 'E']
    #address_list = address.split(' ')
    #street_type = address_list[-1]
    #if get_street_type in exclude_list:
       # street_type = address_list[-2]
    ##return street_type

#street_types = melb_df['Address'].apply(get_street_type)
#print(street_type)
#print(street_types.nunique())
#print(street_types.value_counts())
#popular_stypes = street_types.value_counts().nlargest(10).index
#print(popular_stypes)
#melb_df['StreetType'] = street_types.apply(lambda x: x if x in popular_stypes else 'other')
#print(melb_df['StreetType'])
#print(melb_df['StreetType'].nunique())
#def get_weekend(weekday):
    #if weekday == 5 or weekday == 6:
       # return 1 
    #else:
       # return 0
#melb_df['Weekend'] = melb_df['WeekdaySale'].apply(get_weekend)
#print(round(melb_df[melb_df['Weekend']==1]['Price'].mean(),2))
popular_seler = melb_df['SellerG'].value_counts().nlargest(49).index
melb_df['SellerG'] = melb_df['SellerG'].apply(lambda x: x if x in popular_seler else'other')
#print(melb_df['SellerG'])
a = melb_df[melb_df['SellerG'] == 'Nelson']['Price'].min() 
b = melb_df[melb_df['SellerG'] == 'other']['Price'].min() 
#print(round(a/b, 1))
def get_experience(arg):
    month_key_words = ['месяц', 'месяцев', 'месяца']
    year_key_words = ['год', 'лет', 'года']
    args_splited = arg.split(' ')
    month = 0
    year = 0
    for i in range(len(args_splited)):
        if args_splited[i] in month_key_words:
            month = args_splited[i-1]
        if args_splited[i] in year_key_words:
            year = args_splited[i-1]
    return int(year)*12 + int(month)
unuque_list = []
for col in melb_df.columns:
    item = (col, melb_df[col].nunique(), melb_df[col].dtypes)
    unuque_list.append(item)
    unuque_counts = pd.DataFrame(unuque_list, columns= ['Column_Name', 'Num_Unique', 'Type']).sort_values(by='Num_Unique',  ignore_index=True)
#print(unuque_counts)
cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car'] # список столбцов, которые мы не берём во внимание
max_unique_count = 150 # задаём максимальное число уникальных категорий
for col in melb_df.columns: # цикл по именам столбцов
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude: # проверяем условие
        melb_df[col] = melb_df[col].astype('category') # преобразуем тип столбца
#print(melb_df.info())
#print(melb_df['Regionname'].cat.categories)
#print(melb_df.info)
melcitibike_tr = pd.read_csv('data/citibike-tripdata.csv', sep=',')
#print(melcitibike_tr.isnull().sum())
#print(melcitibike_tr['start station name'].mode()[0])
#print(melcitibike_tr.info())
#print(melcitibike_tr['bikeid'].mode()[0])
mode_usertype = melcitibike_tr['usertype'].mode()[0]
count_mode_user = melcitibike_tr[melcitibike_tr['usertype'] == mode_usertype].shape[0]
#print(round(count_mode_user / melcitibike_tr.shape[0], 2))
#print(mode_usertype)
#print(count_mode_user)
#print(melcitibike_tr[melcitibike_tr['gender']==1])
#print(melcitibike_tr[melcitibike_tr['gender']==2])
#print((melcitibike_tr['start station id']) != (melcitibike_tr['end station id']))  
#melcitibike_tr.drop(['start station id', 'end station id'], axis=1, inplace=True)
#print(melcitibike_tr.shape[1])
#print(melcitibike_tr['birth year'].min())
#print(melcitibike_tr['start station name'].describe())
melcitibike_tr.drop('start station id',axis=1, inplace=True)
melcitibike_tr.drop('end station id', axis=1, inplace=True)
#print(melcitibike_tr.shape[1])
melcitibike_tr['age'] = 2018 - melcitibike_tr['birth year']
melcitibike_tr.drop('birth year', axis=1, inplace=True)
#print(melcitibike_tr[melcitibike_tr['age']>60].shape[0])
melcitibike_tr['starttime'] = pd.to_datetime(melcitibike_tr['starttime'])
melcitibike_tr['stoptime'] = pd.to_datetime(melcitibike_tr['stoptime'])
melcitibike_tr['trip duration'] = (melcitibike_tr['stoptime'] - melcitibike_tr['starttime'])
#print(melcitibike_tr.loc[3, 'trip duration'])
weekday = melcitibike_tr['starttime'].dt.dayofweek
melcitibike_tr['weekend'] = weekday.apply(lambda x: 1 if x ==5 or x == 6 else 0)
#print(melcitibike_tr['weekend'].sum())
def get_time_of_day(time):
    if 0 <= time <= 6:
        return 'night'
    elif 6 < time <= 12:
        return 'morning'
    elif 12 < time <= 18:
        return 'day'
    elif 18 < time <= 23:
        return 'evening'

melcitibike_tr['time_of_day'] = melcitibike_tr['starttime'].dt.hour.apply(get_time_of_day)
a = melcitibike_tr[melcitibike_tr['time_of_day'] == 'day'].shape[0]
b = melcitibike_tr[melcitibike_tr['time_of_day'] == 'night'].shape[0]
print(round(a / b))

    
    



    
    
    
    
    
    
    
