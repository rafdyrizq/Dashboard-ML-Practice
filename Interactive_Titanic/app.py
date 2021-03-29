from flask import Flask, render_template, request

import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np

import json

app= Flask(__name__)



## ## -----------------------  TITANIC  -----------------------------------------------------------

# # Count Plot
# def countplot():
#     titanic=pd.read_csv('C:/Users/LENOVO/Documents/PURWADHIKA/interactive_titanic/static/titanic.csv')
#     data = []

#     hist= go.Histogram(
#         x=titanic['alive'], histfunc='count'
#     )

#     data.append(hist)

#     title = 'Histogram'
#     layout = go.Layout(
#         title='Histogram',
#         xaxis=dict(title='alive')
#     )

#     res = {'data':data, 'layout':layout}

#     graphJSON= json.dumps(res,cls=plotly.utils.PlotlyJSONEncoder)

#     return graphJSON

# @app.route('/')
# def count_fn_titanic():
#     plot=countplot()
#     return render_template('index.html',plot=plot)



# Box Plot
def boxplot():
    titanic=pd.read_csv('C:/Users/LENOVO/Documents/PURWADHIKA/interactive_titanic/static/titanic.csv')
    data = []

    box = go.Box(
        x=titanic['fare']
    )

    data.append(box)

    layout = go.Layout(
        title='Box',
        xaxis=dict(title='fare')
    )

    res = {'data':data, 'layout':layout}

    graphJSON= json.dumps(res,cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/')
def box_fn():
    plot=boxplot()
    return render_template('index.html',plot=plot)


if __name__== '__main__':
    app.run(debug=True)


## ## -----------------------  CONTOH TIPS  -----------------------------------------------------------

## ## ----------------------------------------
# # Scatter Plot
# def scatter_plot():
#     dfTips=pd.read_csv('./static/tips.csv')

#     data=[]
#     scatt= go.Scatter(
#         x=dfTips['tip'],
#         y=dfTips['total_bill'],
#         mode='markers'
#     )

#     data.append(scatt)

#     layout= go.Layout(
#         title='Scatter',
#         title_x=0.5,
#         xaxis=dict(title='tip'),
#         yaxis=dict(title='total_bill')
#     )

#     res={'data':data, 'layout':layout}

#     graphJSON= json.dumps(res,cls=plotly.utils.PlotlyJSONEncoder)

#     return graphJSON

# @app.route('/')
# def scatt_fn():
#     plot=scatter_plot()
#     return render_template('index.html',plot=plot)

# C:\Users\LENOVO\Documents\PURWADHIKA\interactive_plotting

## ## ----------------------------------------

# # Histogram
# def histogram():
#     dfTips=pd.read_csv('C:/Users/LENOVO/Documents/PURWADHIKA/interactive_plotting/static/tips.csv')
#     data=[]

#     hist= go.Histogram(
#         x=dfTips['tip'], histfunc='count'
#     )

#     data.append(hist)

#     title = 'Histogram'
#     layout = go.Layout(
#         title='Histogram',
#         xaxis=dict(title='tip')
#     )

#     res = {'data':data, 'layout':layout}

#     graphJSON= json.dumps(res,cls=plotly.utils.PlotlyJSONEncoder)

#     return graphJSON

# @app.route('/')
# def hist_fn():
#     plot=histogram()
#     return render_template('index.html',plot=plot)



## ## ----------------------------------------

# # Pie Plot
# def pie_plot():
#     dfTips=pd.read_csv('C:/Users/LENOVO/Documents/PURWADHIKA/interactive_plotting/static/tips.csv')

#     vcounts= dfTips['day'].value_counts()

#     labels=[]
#     values=[]

#     for item in vcounts.iteritems():
#         labels.append(item[0])
#         values.append(item[1])

#     data = [go.Pie(
#         labels=labels,
#         values=values
#     )]

#     layout = go.Layout(
#         title='Pie',
#         title_x=0.48
#     )

#     res = {'data':data, 'layout':layout}

#     graphJSON= json.dumps(res,cls=plotly.utils.PlotlyJSONEncoder)

#     return graphJSON

# @app.route('/')
# def pie_fn():
#     plot=pie_plot()
#     return render_template('index.html',plot=plot)


## ## ----------------------------------------

# # Box Plot
# def boxplot():
#     dfTips=pd.read_csv('C:/Users/LENOVO/Documents/PURWADHIKA/interactive_plotting/static/tips.csv')
#     data = []

#     box = go.Box(
#         x=dfTips['total_bill']
#     )

#     data.append(box)

#     layout = go.Layout(
#         title='Box',
#         xaxis=dict(title='total_bill')
#     )

#     res = {'data':data, 'layout':layout}

#     graphJSON= json.dumps(res,cls=plotly.utils.PlotlyJSONEncoder)

#     return graphJSON

# @app.route('/')
# def box_fn():
#     plot=boxplot()
#     return render_template('index.html',plot=plot)


