pandas.read_sql_table(table_name,con,schema=None,index_col=None,coerce_float=True,
columns=None)
pandas.read_sql_Query(sql, con, index_col=None, coerce_float=True)
pandas.read_sql(sql, con, index_col=None, coerce_float=True, columns=None)

import pandas as pd
formlist = pd.read_sql_query('show table', con = engine)
print('testdb'','\n',formlist)

import pandas as pd
import numpy as ny
df = pd.read_csv("/Users/Will/Downloads/test_assets.csv")

df.dtypes
df.to_csv("/Users/Will/Downloads/test_assets.csv",index=False)
merged = pd.merge(w1, w2)

merged = pd.merge(w1,w2)
merged_all = pd.merge(merged,w3,left_on="name",right_on="merchant_id")

qn = pd.DataFrame(columns=('BIN', 'Boro Code', 'Boro', 'House Number', 'Street Name', 'Address', 'Latitude', 'Longitude'))


df = df.T
pd.set_option('chained_assignment', None)
geoCodeCheck = geoCodeCheck[geoCode['Street Name'] == 'knickerbocker avenue']

mask = (dfList['XCoord'] >= xy2[0]) & (dfList['YCoord'] <= xy1[0])
dfList_subset = dfList.loc[mask]

df2 = df[df2.Addres.str.contains("WEST END AVE") == False]
df = df[(df['closing_price'] >= 99) & (df['closig_price'] <= 101)]

df = df[df['Name'].isin(nameList)]
dpsub = dp[~dp['BIN'].isin(binList)]

df2 = df[df['INSPECTION_ID'] == df["INSPECTION_ID.1"]]
only_gold = df[df['Gold'] > 0]

export = export.sort_values(by = 'High Risk Ranking',ascending = False).reset_index(drop = False)
sorted(ratio_list, reverse = True)

ids = dfInt["NODEID"]
dfInt2 = dfInt[ids.isin(ids[ids.duplicated()])].sort_values(by = "NODEID")

ratio_list = sorted(ratio_list, key = itemgetter(1), reverse = True)
df = df.reindex_axis(sorted(columns),axis = 1)

df = pd.DataFrame(dfList, columns = ['BIN', 'Boro', 'Address'])
list_block = []
for i in r