import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv(r"C:\\Users\\chand\Downloads\\NTRS (1).csv")

data.sort_values("Date", inplace=True)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "NTRS TEAM 12"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="ηorthern Trust", className="header-emoji"),
                html.H1(
                    children="Currency Chart", className="header-title"
                ),
                html.P(
                    children="Analysis of differenct Currencies "
                    "keeping the Base as the US Dollar"
                    " from 2012 and 2022",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["Australian dollar   (AUD)                     "],
                                    "type": "lines"
                                                                   },
                            ],
                            "layout": {
                                "title": {
                                    "text": "USD to Austrailian Dollar                                                                                1 USD = 1.54 Australian Dollar",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "AUS$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17B897"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["Indian rupee   (INR)                     "],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "USD TO INDIAN RUPEES                                                                        1 US Dollar = 81.49 Indian Rupee",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),




                
                                html.Div(
                    children=dcc.Graph(
                        id="volume1-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["Canadian dollar   (CAD)                     "],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "USD TO CAD                                                                                                       1 USD = 1.35 CAD",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#698e18"],
                            },
                        },
                    ),
                    className="card",
                ),



                                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["Brazilian real   (BRL)                     "],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "USD TO BRL                                                                                              1 USD = 5.14 Brazilian Real",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#59076b"],
                            },
                        },
                    ),
                    className="card",
                ),



        
                                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["Japanese yen   (JPY)                     "],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "USD TO YEN                                                                                                      1 USD = 145.86 YEN",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#c77191"],
                            },
                        },
                    ),
                    className="card",
                ),





            

            ],
            className="wrapper",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)