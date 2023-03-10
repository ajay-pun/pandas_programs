import pandas as pd


#----------------------------------------------------------------------------------
#creating pandas dataframe
df=pd.DataFrame(data_list,columns=column_list)           #data_list=[ list1,  list2,  ...listN]


#-----------------------------------------------------------------------------------
#getting the no of row
n=len(df.index)


#------------------------------------------------------------------------------------
#adding a new row
df.iloc[len(df.index)]=list       

"""we can also use loc instead of iloc.
loc uses actual index of item in the list.
iloc uses index column or indexing of data.

Note: We cannot use iloc when there is no index column."""


#-------------------------------------------------------------------------------------
#editing a row
df.iloc[len(df.index)-1]=list                            #we have edited the last row

"""similary we can also use loc for this task
  we can edit any row by using index"""


#-------------------------------------------------------------------------------------
#getting the column
df.column_name

"""we can convert the column into any structures for eg,
    dict(df.column_name)
    list(df.column_name)"""
