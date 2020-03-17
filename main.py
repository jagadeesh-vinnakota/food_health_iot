import dash
import dash_core_components as dcc
import dash_html_components as html
from data_gather import plot_line_graph
from run_save_model import predict_line_graph, train_save_load
from generating_data import generate_sensors_data

# generating sensors data
generate_sensors_data()
train_save_load()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Graph(id='g1', figure=plot_line_graph(warehouse_name='wh1', warehouse_zone='zone1', title="Gerogia warehouse zone 1 present health"))
        ], className="six columns"),

        html.Div([
            dcc.Graph(id='g2', figure=predict_line_graph(warehouse_name='wh1', warehouse_zone='zone1', title="Gerogia warehouse zone 1 future health"))
        ], className="six columns"),
    ], className="row"),

    html.Div([
        html.Div([
            dcc.Graph(id='g3', figure=plot_line_graph(warehouse_name='wh1', warehouse_zone='zone2', title="Georgia warehouse zone 2 present health"))
        ], className="six columns"),

        html.Div([
            dcc.Graph(id='g4', figure=predict_line_graph(warehouse_name='wh1', warehouse_zone='zone2', title="Georgia warehouse zone 2 future health"))
        ], className="six columns"),
    ], className="row")

])


if __name__ == '__main__':
    app.run_server(debug=False)