from fbprophet import Prophet
import pickle
import pandas as pd
import plotly.graph_objects as go
import os


def train_and_save(warehouse_name, warehouse_zone):
    file = os.path.join(".",warehouse_name,warehouse_zone,"warehousedata.csv")
    warehouse_zone_data = pd.read_csv(file)
    warehouse_zone_data['date'] = pd.to_datetime(warehouse_zone_data.date)
    warehouse_zone_data.rename(columns={"date":"ds", "average_temparature":"y"}, inplace=True)
    mod_prophet = Prophet(interval_width=0.95, yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
    mod_prophet.fit(warehouse_zone_data)
    with open(os.path.join(".",warehouse_name,warehouse_zone,"warehousedata"), "wb") as f:
        pickle.dump(mod_prophet, f)


def fix_scores(score):
    return score+4

def fix_scores_upper(score):
    return score-4


def load_and_predict(warehouse_name, warehouse_zone):
    file = os.path.join(".",warehouse_name,warehouse_zone,"warehousedata")
    with open(file, "rb") as f:
        loaded_forecaster = pickle.load(f)
    future = loaded_forecaster.make_future_dataframe(periods=336, freq='30T')
    forecast = loaded_forecaster.predict(future)
    data_final = forecast.tail(336)
    data_final['yhat_lower'] = data_final['yhat_lower'].apply(fix_scores)
    data_final['yhat_upper'] = data_final['yhat_upper'].apply(fix_scores_upper)
    data_final.to_csv(os.path.join(".",warehouse_name,warehouse_zone,"warehousedata_predictions.csv"), header=True, index=False)


def train_save_load():
    train_and_save(warehouse_name='wh1', warehouse_zone='zone1')
    load_and_predict(warehouse_name='wh1', warehouse_zone='zone1')

    train_and_save(warehouse_name='wh1', warehouse_zone='zone2')
    load_and_predict(warehouse_name='wh1', warehouse_zone='zone2')

    train_and_save(warehouse_name='wh2', warehouse_zone='zone1')
    load_and_predict(warehouse_name='wh2', warehouse_zone='zone1')

    train_and_save(warehouse_name='wh2', warehouse_zone='zone2')
    load_and_predict(warehouse_name='wh2', warehouse_zone='zone2')

    train_and_save(warehouse_name='wh3', warehouse_zone='zone1')
    load_and_predict(warehouse_name='wh3', warehouse_zone='zone1')

    train_and_save(warehouse_name='wh3', warehouse_zone='zone2')
    load_and_predict(warehouse_name='wh3', warehouse_zone='zone2')

    train_and_save(warehouse_name='wh4', warehouse_zone='zone1')
    load_and_predict(warehouse_name='wh4', warehouse_zone='zone1')

    train_and_save(warehouse_name='wh4', warehouse_zone='zone2')
    load_and_predict(warehouse_name='wh4', warehouse_zone='zone2')


def predict_line_graph(warehouse_name, warehouse_zone, title):
    file = os.path.join(".",warehouse_name,warehouse_zone,"warehousedata_predictions.csv")
    data_final = pd.read_csv(file)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data_final['ds'],
        y=data_final['yhat'],
        name="Actual Temparature",
        line_color='green',
        opacity=0.8))

    # fig.add_trace(go.Scatter(
    #     x=data_final['ds'],
    #     y=data_final['yhat_upper'],
    #     name="High Temparature",
    #     line_color='red',
    #     opacity=0.8))
    #
    # fig.add_trace(go.Scatter(
    #     x=data_final['ds'],
    #     y=data_final['yhat_lower'],
    #     name=" Low Temparature",
    #     line_color='blue',
    #     opacity=0.8))
    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Temparature in Farenheit",
    )
    return fig
