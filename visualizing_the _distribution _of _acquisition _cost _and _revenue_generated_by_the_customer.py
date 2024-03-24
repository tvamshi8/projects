import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv('c:\\Users\\vamsh\\Downloads\\acquisition_data\\customer_acquisition_data.csv')


fig = px.histogram(data, 
                   x="cost", 
                   nbins=20, 
                   title='Distribution of Acquisition Cost')
fig.show()

fig = px.histogram(data, 
                   x="revenue", 
                   nbins=20, 
                   title='Distribution of Revenue')
fig.show()