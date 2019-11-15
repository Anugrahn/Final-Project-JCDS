import plotly
import plotly.graph_objects as go
import pandas as pd
import json
from datas import data_clean

def quadrant_plots():
    df = data_clean()
    df_group = df.QUADRANT.value_counts()
    fig = go.Figure([go.Bar(x=df_group.index, y = df_group.values)])
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def ward_plots():
    df = data_clean()
    df_group2 = df.WARD.value_counts()
    fig = go.Figure([go.Bar(x=df_group2.index, y = df_group2.values)])
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

