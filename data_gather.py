import plotly.graph_objects as go
import pandas as pd
import datetime
import os


today = datetime.date.today()
end_date = datetime.date.today()
start_date = today - datetime.timedelta(days = 7)


def mask_lastweek_data(warehouse_name, warehouse_zone):
    file = os.path.join(".",warehouse_name,warehouse_zone,"warehousedata.csv")
    warehouse_zone_data = pd.read_csv(file)
    warehouse_zone_data['date'] = pd.to_datetime(warehouse_zone_data.date)
    mask_data = (warehouse_zone_data['date'].dt.date > start_date) & (warehouse_zone_data['date'].dt.date <= end_date)
    warehouse_mask_data = warehouse_zone_data.loc[mask_data]
    return warehouse_mask_data


def plot_line_graph(warehouse_name, warehouse_zone, title):
    warehouse_mask_data = mask_lastweek_data(warehouse_name=warehouse_name, warehouse_zone=warehouse_zone)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
                    x=warehouse_mask_data.date,
                    y=warehouse_mask_data.average_temparature,
                    name="Temparature",
                    line_color='blue',
                    opacity=0.8))

    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Temparature",
    )
    return fig
