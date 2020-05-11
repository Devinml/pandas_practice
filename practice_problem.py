import pandas as pd
import numpy as np
'''
Write a Pandas program to create and display a DataFrame from a specified dictionary data which 
has the index labels
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
'''
exam_data = {'name':['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data=exam_data,index= labels)
#print(df.head())
#print(df.info())

'''
Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
 Go to the editor
Sample Python dictionary data and list labels:
'''
#print(df[['name','score']])

'''
 Write a Pandas program to select the specified columns and rows from a given data frame. 
 Go to the editor
Sample Python dictionary data and list labels:
Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.
'''
#print(df)
#print(df[['name','score']].iloc[[1,3,5,6]])

'''
Write a Pandas program to select the rows where the number of attempts in the examination is 
greater than 2. Go to the editor
Sample Python dictionary data and list labels:
'''
#print(df.loc[df['attempts']>2])

'''
Write a Pandas program to count the number of rows and columns of a DataFrame. Go to the editor
Sample Python dictionary data and list labels:
'''
#num_of_rows = len(df)
#num_of_columns = len(df.columns)
#print(f'number of Rows = {num_of_rows}')
#print(f'number of Columns = {num_of_columns}')

'''
Write a Pandas program to select the rows where the score is missing, i.e. is NaN. Go to the editor
Sample Python dictionary data and list labels:
'''

#print(df.loc[df['score'].isnull()])

'''
Write a Pandas program to select the rows the score is between 15 and 20 (inclusive). Go to the editor
Sample Python dictionary data and list labels:
'''
#print(df[(df['score'] >= 15) & (df['score']<= 20)])

'''
 Write a Pandas program to select the rows where number of attempts in the examination is 
 less than 2 and score greater than 15
'''

#print(df[(df['attempts'] < 2)&(df['score'] > 15)])

'''
Write a Pandas program to change the score in row 'd' to 11.5. Go to the editor
Sample Python dictionary data and list labels:
'''
#df.loc['d','score'] = 11.5
#print(df.loc['d','score'])

'''
Write a Pandas program to calculate the sum of the examination attempts by the students. Go to the editor
Sample Python dictionary data and list labels:
'''

#print(df['attempts'].sum())

'''
Write a Pandas program to calculate the mean score for each different student in DataFrame. Go to the editor
Sample Python dictionary data and list labels:
'''

#print(df['score'].mean())

'''
Write a Pandas program to append a new row 'k' to data frame with given values for each column.
 Now delete the new row and return the original DataFrame
'''
#row_k = {'name':'Jim','score': 20, 'attempts': 100, 'qualify':'yes'}
#df.loc['k'] = row_k
#print(df)
#df.drop('k',inplace=True)
#print(df.tail())

'''
Write a Pandas program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order. Go to the editor
Sample Python dictionary data and list labels:
'''
#print(df.sort_values(by = ['name','score'],ascending=[False,True]))

'''
Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False. Go to the editor
Sample Python dictionary data and list labels:
'''

#def yes_to_true(input_string):
#    if 'yes' in input_string:
#        return True
#    else:
#        return False
#df['qualify'] = df['qualify'].apply(lambda x : yes_to_true(x))
#print(df)

'''
Write a Pandas program to change the name 'James' to 'Suresh' in name column of the DataFrame. Go to the editor
Sample Python dictionary data and list labels:
'''
#df.loc[df['name'] == 'James','name'] = 'Suresh'
#print(df.loc['d'])

'''
Write a Pandas program to delete the 'attempts' column from the DataFrame. Go to the editor
Sample Python dictionary data and list labels:
'''
#df.pop('attempts')
#print(df)

'''
Write a Pandas program to insert a new column in existing DataFrame. Go to the editor
Sample Python dictionary data and list labels:
'''
#df['color'] = ['Red','Blue','Green','Violet','Rainbow','Orange','Magenta','Pink','Black','White']
#print(df)

'''

'''

