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
