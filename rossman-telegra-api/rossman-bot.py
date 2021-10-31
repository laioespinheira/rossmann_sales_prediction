import requests
import json
import pandas as pd

def load_dateset( store_id ):
	# loading test dataset
	df10 = pd.read_csv('/Users/iCone/Repos/DataScience_Em_Producao/data/test.csv')
	df_store_raw = pd.read_csv('/Users/iCone/Repos/DataScience_Em_Producao/data/store.csv')

	# merge test dataset + store
	df_test = pd.merge( df10, df_store_raw, how='left', on='Store' )

	# choose store for prediction
	df_test = df_test[df_test['Store'] == 22] 

	# remove closed days
	df_test = df_test[df_test['Open'] != 0]
	df_test = df_test[~df_test['Open'].isnull()]
	df_test = df_test.drop('Id', axis=1)
	
	# convert DataFrame to json
	data = json.dumps(df_test.to_dict( orient='records') )

	return data

def predict( data ):

	# API Call
	url = 'https://rossman-model-test-laio.herokuapp.com/rossman/predict'
	header = {'Content-type': 'application/json'}
	data = data
	
	r = requests.post( url, data=data, headers=header)
	print('Status Code {}'.format( r.status_code ) )
	
	d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys() )
	
	return d1

#d2 = d1[['store', 'prediction']].groupby('store').sum().reset_index()

#for i in range(len(d2)):
#    print('Store Number {} will sell {:,.2f} in the next 6 weeks'.format(
#           d2.loc[i, 'store'], 
#           d2.loc[i, 'prediction'] ) )
