import pandas as pd
def create_medications(names, counts):
    medications = pd.Series(index=names, data=counts)
    return medications
def get_percent(medications, name):
    return(medications.loc[name]/sum(medications) * 100)


names=['chlorhexidine', 'cyntomycin', 'afobazol']
counts=[15, 18, 7]
print(create_medications(names = ['chlorhexidine', 'cyntomycin', 'afobazol'], counts = [26, 18, 7]))
