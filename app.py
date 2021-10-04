import dash
import pymongo
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output

from pymongo import MongoClient
uri =  "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.end1o.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(uri)

db = client.sample_analytics
collection = db.transactions

data = pd.DataFrame(list(db.transactions.find()))

data1= collection.count_documents({"transaction_count": 10})
data2= collection.count_documents({"transaction_count": 20})
data3= collection.count_documents({"transaction_count": 30})
data4= collection.count_documents({"transaction_count": 40})
data5= collection.count_documents({"transaction_count": 50})
data6= collection.count_documents({"transaction_count": 60})
data7= collection.count_documents({"transaction_count": 70})
data8= collection.count_documents({"transaction_count": 80})
data9= collection.count_documents({"transaction_count": 90})
data10= collection.count_documents({"transaction_count": 100})

labels = ['10 transactions', '20 transactions', '30 transactions', '40 transactions', '50 transactions', 
'60 transactions', '70 transactions', '80 transactions', '90 transactions', '100 transactions']

values = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()