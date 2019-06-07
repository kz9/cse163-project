import pandas as pd
import pandas_bokeh
from bokeh.plotting import figure
from bokeh.layouts import column, row, WidgetBox
from bokeh.models import Panel
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import RangeSlider, Slider


def effect_tab(df):
    year = Slider(start=1970, end=2017, value=1970, step=1,
                       title="Year Range")

    def make_data(df, year=1970):
        modified = df[df['iyear'] == year].groupby(
                'imonth', as_index=False)['eventid'].count()
        return ColumnDataSource(modified)

    def update():
        new_src = make_data(df, year.value)
        src.data.update(new_src.data)

    year.on_change('value', lambda attr, old, new: update())
    src = make_data(df)

    TOOLTIPS = [
        ('Month', '@imonth'),
        ('Counts', '@eventid')
    ]

    p = figure(plot_height=800, plot_width=800,
               title='Total attacks over years by month',
               x_axis_label='Month',
               y_axis_label='Attacks',
               tooltips=TOOLTIPS,
               output_backend="webgl")
    p.line(x='imonth', y='eventid', source=src, line_width=2, color='red')
    p.circle(x='imonth', y='eventid', source=src, size=8, fill_color='white')

    tab = Panel(child=row(year, p), title='Year Effect Attacks')

    return tab
