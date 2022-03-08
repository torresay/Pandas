import pandas as pd

# READING OF DATAFRAMES AND ITS ATTRIBUTES

# Access to table data

# Head(n) method: show us the firsts n values of the table
pd.options.display.max_rows = 8
data = pd.read_excel('AAPL.xlsx', sheet_name='Hoja1')
data.head(3)  # show the  3 first rows

# Tail(n) method: show us the last n values of the table
data.tail(4)

# LOC & ILOC Methods
# loc --> names of the elements
# iloc --> index of the element

print(data.loc[2])
print(data.iloc[2])
# in this case it shows the same element because our index it´s a number

pd.options.display.max_rows = 8
data = pd.read_excel('AAPL.xlsx', sheet_name='Hoja1')
dataIndexDate = data.set_index('timestamp')
print(dataIndexDate)
# now for the iloc method its the same as before, because this method calls the n element of the table, doesn't depend on the index
print(dataIndexDate.iloc[2])

# now for the loc method we can't call the element 2, because it doesnt exists anymore, so we have to put a date that i want that return
print(dataIndexDate.loc['2020-03-04'])

# We select some elements of the table
# For that we ask for a list of elements separates by a coma
data.iloc[[2, 4]]

# We select a range of rows inside the table
data.loc[2:4]
# But if we used :
data.iloc[2:4]
# it will show us a different output, because the loc method calls the names, (the elements that are 2, 3 or 4), but the iloc method calls the index, and then it applies a certain criteria, including the first element but not the last.


# SELECTING COLUMNS
data.loc[:,['timestamp', 'close']]  # Here we watch everything on the terminal

data.loc[0:2, ['timestamp', 'close', 'volume']] # We only see the first three rows
data.iloc[0:2, [0, 4, 6]]  # Shows the first two rows
data.tail(3).loc[:,['timestamp', 'close', 'volume']]  #access the last three rows
data.tail(3).loc[::-1, ['timestamp', 'close', 'volume']]  # We access to the three last rows ordered in reverse



