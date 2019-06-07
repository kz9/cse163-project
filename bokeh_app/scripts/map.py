import pandas as pd
import hvplot.pandas
from os.path import dirname, join, basename
import pandas_bokeh
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show, output_file
from bokeh.models.glyphs import ImageURL
from bokeh.layouts import column, row, WidgetBox, layout
from bokeh.models import Panel, ColumnDataSource, HoverTool, LogColorMapper
from bokeh.palettes import RdYlBu11 as palettes
from bokeh.transform import factor_cmap
from bokeh.models.tools import CustomJSHover
from bokeh.models.widgets import RangeSlider, CheckboxGroup, Div


def map_tab(df, shp):
    def make_data(gdf, shp, start=1970, end=2017):
        modified = df[(df['iyear'] >= start) &
                      (df['iyear'] <= end)]
        modified = modified.groupby(['country_txt', 'iyear'],
                                    as_index=False)['eventid'].count()
        temp = pd.DataFrame()
        temp['country_txt'] = modified.country_txt.unique()
        for i in range(start, end + 1):
            data = modified[
                    modified['iyear'] <= i].groupby(
                    'country_txt', as_index=False)[
                            'eventid'].sum()
            if len(data) != len(temp.country_txt):
                counts = []
                for j in temp.country_txt:
                    if j in list(data.country_txt):
                        counts.append(
                                int(data[data['country_txt'] == j]['eventid']))
                    else:
                        counts.append(0)
                temp['year_{}'.format(i)] = counts
            else:
                temp['year_{}'.format(i)] = data['eventid']
        modified = shp.merge(temp, right_on='country_txt',
                             left_on='SOVEREIGNT', how='inner')
        return modified

    src = make_data(df, shp)
    slider_columns = ['year_{}'.format(i) for i in range(1970, 2018)]

    srange = range(1970, 2018)

    p = src.plot_bokeh(
        figsize=(900, 600),
        simplify_shapes=5000,
        slider=slider_columns,
        slider_range=srange,
        slider_name="Year",
        colormap='Viridis',
        hovertool_columns=['country_txt'],
        title="Cumulative Attacks Map")

    tab = Panel(child=row(p), title='Cumulative Map')

    return tab
