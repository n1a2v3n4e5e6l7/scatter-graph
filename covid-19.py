import pandas as pv
import plotly.express as px
df = pv.read_csv("Copy+of+data+-+data.csv")
fig = px.scatter(df,x = 'date',y = 'cases',color = "country",)
fig.show()