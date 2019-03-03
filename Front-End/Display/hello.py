import pandas as pd
import plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout, Data, Figure

from datetime import datetime

data = pd.read_csv("ldr.csv")
        


countmovies= len(list(data))
#data.seek(0)

def Cloning(li1): 
    li_copy = list(li1) 
    return li_copy

#data.seek(0)


random_x = data['Day']
random_y = data['Percent']
layoutt = go.Layout(
    title='Percentage of Light on LDR in a given day',
    xaxis=dict(
        title='Days',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Percent of Light of LDR',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)



# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y,
    name ='GG'
    
    
    )
data=[trace]
fig = go.Figure(data, layout=layoutt)

py.offline.plot(fig, filename='genre_splitup.html',auto_open=False)
print("Generated Genre Splitup")