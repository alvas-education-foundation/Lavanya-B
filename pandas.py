
# github repository- Lavanya-B


import pandas as pd

data = [
['r1', '11', '30', 'am', '9', 'pm'],
['r2', '11', '30', 'am', '9', '30', 'pm'],
['r3', '11', 'am', '12', '30', 'am'],
['r4', '11', 'am', '10', 'pm']]


df = pd.DataFrame(data)
print(df)


for index, row in df.iterrows():
    if row[2] in ('am', 'pm'):
        df.iloc[[index],3:7] = df.iloc[[index],2:6].values.tolist()
        df.iloc[[index],[2]] = '00'
    if row[5] in ('am', 'pm'):
        df.iloc[[index],[6]] = df.iloc[[index],[5]].values.tolist()
        df.iloc[[index],[5]] = '00'

df.columns = ['entity', 'b_hour', 'b_min', 'b_ampm', 'e_hour', 'e_min', 'e_ampm']
print(df)


df['open'] = df['b_hour'] + ':' + df['b_min'] + " " + df['b_ampm']
df['close'] = df['e_hour'] + ':' + df['e_min'] + " " + df['e_ampm']


print(df.loc[:, ['entity', 'open', 'close']])