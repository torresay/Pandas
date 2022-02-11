import pandas as pd

data = pd.read_csv("AAPL.csv", sep=",")
print(data)

data1 = pd.read_csv("SPY.csv", sep=";")
print(data1)

data2 = pd.read_excel("AAPL.xlsx", sheet_name="Hoja1")
print(data2)

data2_1 = pd.read_excel("AAPL.xlsx", sheet_name= "Hoja1", index_col="timestamp")
print(data2_1)

columnas = ["timestamp", "open", "close"]
data2_2 = pd.read_excel("AAPL.xlsx", sheet_name="Hoja1", index_col="timestamp", usecols=columnas)
print(data2_2)

# Configure the output
pd.options.display.max_rows = 4
pd.options.display.max_columns = 6
data2_3 = pd.read_excel("AAPL.xlsx", sheet_name="Hoja1")
print(data2_3)

# if we want that the number of rows or columns are unlimited --> None
pd.options.display.max_columns = None
pd.options.display.max_rows = 6
# print(data)

# Format Options
pd.options.display.precision = 4
pd.options.display.precision = 2
print(data2_3)

# General information of the dataFrame
print(data2_3.info())
print('-' * 80)
print(data2_3.shape)  # rows, columns
print('-' * 80)
print(data2_3.columns)  # shows the columns names
print(list(data2_3.columns))  # I also could modified the columns
print('-' * 80)
print(data2_3.dtypes)  # like a dictionary
print(dict(data2_3.dtypes))

# datFrames index
# Setting the index --> usually dates or a crescent number
data2_3.set_index('timestamp', inplace=True)  # inplace assign the setting in the same line
print(data2_3)

# the attribute 'drop' remove the column of the last index
data2_3 = data2_3.reset_index()
print(data2_3)
data2_3 = data2_3.reset_index(drop=True)
print('-' * 80)

# Create new Columns
data3 = pd.read_excel('AAPL.xlsx', sheet_name='Hoja1')
data3['Precio_COME'] = 3
data3.drop(['high', 'low'], axis=1).head()  # this allows me to see the table better
data3.set_index('timestamp', inplace=True)
print(data3)

# Create a new column based in other columns
data4 = pd.read_excel('AAPL.xlsx', sheet_name='Hoja1')
data4.set_index('timestamp', inplace=True)
data4['precio_medio'] = (data4.open + data4.close + data4.low + data4.high)/4
data4.drop(['high', 'low'], axis=1).head()

# now we are going to create a new column that show the daily volume in million dollars
data5 = pd.read_excel('AAPL.xlsx', sheet_name='Hoja1')
data5.set_index('timestamp', inplace=True)
data5['precio_medio'] = (data5.open + data5.close + data5.low + data5.high)/4
data5['vol_min_usd'] = round((data5.volume * data5.precio_medio) / 1000000)
data5.drop(['open', 'high', 'low', 'close'], axis=1).head()
print(data5)

# Creating a new column iterating the dataFrame
data6 = pd.read_excel("AAPL.xlsx", sheet_name='Hoja1')

for i in range(len(data6)):
    if data6.loc[i, 'close'] > data6.loc[i, 'open']:
        data6.loc[i, 'color_vela'] = 'verde'
    else:
        data6.loc[i, ' color_vela'] = 'roja'

data6.drop(['high', 'low'], axis=1).head(8)

# Saving a dataframe to an excel
data7 = pd.read_excel("AAPL.xlsx", sheet_name='Hoja1')
data7['mov_intra'] = data7.close - data7.open
data7.drop(['high', 'low', 'adjusted_close'], axis=1). head()
data7.to_excel('AAPL_Modificado.xlsx', sheet_name='HojaEjemplo')

# Creating a dataframe based on a list of lists
data = [["ALUA", 19.15], ["BBAR", 73.70], ["BMA", 144.4], ["BYMA", 234]]
tabla = pd.DataFrame(data, columns=['Ticket', 'Precio'])
print(tabla)

# Creating a dataframe based on a dictionary
data_dict = {'Tickers': ['ALUA', 'BBAR', 'BMA', 'BYMA'], 'Precios': [19.15, 73.7, 144.4, 234]}
tabla_dict = pd.DataFrame(data_dict)
print(tabla_dict)

# we could put a personalize index
data_ind = {

    'Tickers': ["ALUA", "BBAR", "BMA", "BYMA"],
    'Precios': [19.15, 73.7, 144.4, 234]

}
tabla_ind = pd.DataFrame(data, index=["activo_1", "activo_2", "activo_3", "activo_4"])
print(tabla_ind)

# Creating in based of a list of dictionaries
data_dict = [

    {"ticker": "ALUA", "Precio": 19.15, "Tipo": "Action"},

    {"ticker": "BBAR", "Precio": 73.7, "Tipo": "Accion"},

    {"ticker": "BMA", "Precio": 144.4},

    {"ticker": "BYMA", "Precio": 234, "Tipo": "Accion"},

 ]
tabla_list_dict = pd.DataFrame(data_dict)
print(tabla_list_dict)

# Also I can create it defining the columns that I want
data_dict_2 = [

    {"ticker": "ALUA", "Precio": 19.15, "Tipo": "Action"},

    {"ticker": "BBAR", "Precio": 73.7, "Tipo": "Accion"},

    {"ticker": "BMA", "Precio": 144.4},

    {"ticker": "BYMA", "Precio": 234, "Tipo": "Accion"},

 ]
tabla_list_dict_2 = pd.DataFrame(data, columns=['ticker', 'Precio'])
print(tabla_list_dict_2)

# Creating based on another dataframe
data_of_df = pd.read_excel('AAPL.xlsx', sheet_name='Hoja1')
copy = data_of_df[['timestamp', 'open', 'close']].copy().set_index('timestamp')
print(copy.head(4))

# now with the filter method
data = pd.read_excel('AAPL.xlsx', sheet_name="Hoja1")
copy_2 = data.filter(["timestamp", "open", "close"]).set_index("timestamp")
print(copy_2.head(4))

# and the last way would be to do it taking the original but without the columns that we don't want
data_less_col = pd.read_excel('AAPL.xlsx', sheet_name="Hoja1")
copia_drop = data_less_col.drop(['high', 'low', 'adjusted_close'], axis=1)
print(copia_drop)


# ¡¡¡EXERCISES!!!

# 1
data_exer = pd.read_excel('AAPL.xlsx', sheet_name='Hoja1')
data_exer['var_intra'] = (data_exer.close / data_exer.open) * 100
print(data_exer)

# 2
pd.options.display.precision = 2
pd.options.display.max_columns = None
pd.options.display.max_rows = 4
print(data_exer)

# 3
data_exer.to_excel('AAPL_ej_aylen', sheet_name='Ej3', columns=['timestamp', 'var_intra'])

