import plotly.express as px


def create_map_figure(df, sqft_col=None):
     # Creates a Plotly figure object with the data from the DF. 
     #If the 'sqft' column is specified, it is used to size the markers on the map.
    if sqft_col:
        fig = px.scatter_mapbox(
            df,
            lat="latitude",
            lon="longitude",
            hover_name="Name",
            color="Name",
            size="sqft",
            color_continuous_scale="Viridis",
            mapbox_style="carto-positron",
        )
    else:
        fig = px.scatter_mapbox(
            df,
            lat="latitude",
            lon="longitude",
            hover_name="Name",
            color="Name",
            color_continuous_scale="Viridis",
            mapbox_style="carto-positron",
        )
    return fig


def show_map(fig):
    fig.show()
