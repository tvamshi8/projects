import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv("C:\\Users\\vamsh\\Downloads\\acquisition_data\\customer_acquisition_data.csv")
print(data.head())