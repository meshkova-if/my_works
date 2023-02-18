import pandas as pd
melb_data = pd.read_csv('data/melb_data_fe.csv')
melb_data.head()
#print(melb_data.info())
melb_data['Date']= pd.to_datetime(melb_data['Date'])
#print(melb_data.info())
melb_data['Date'] = melb_data['Date'].dt.quarter
#print(melb_data['Date'].value_counts())
cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car']
max_unique_count = 150
for col in melb_data.columns:
    if melb_data[col].nunique()<max_unique_count and col not in cols_to_exclude:
        melb_data[col] = melb_data[col].astype('category')
print(melb_data.info('category'))
        