import numpy as np
import plotly
import json
import plotly.graph_objs as go

def try1():
    count = 500
    xScale = np.linspace(0, 100, count)
    yScale = np.random.randn(count)

    # Create a trace
    trace = go.Scatter(
        x=xScale,
        y=yScale
    )

    data = [trace]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON