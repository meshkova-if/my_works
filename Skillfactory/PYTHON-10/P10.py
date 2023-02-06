#import pandas as pd
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

