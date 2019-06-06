import pandas as pd
import pandas_bokeh
from bokeh.plotting import figure
from bokeh.layouts import column, row, WidgetBox
from bokeh.models import Panel
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import RangeSlider


def total_tab(df):
    year = RangeSlider(start=1970, end=2017, value=(1970, 2017), step=1,
                       title="Year Range")

    def make_data(df, start=1970, end=2017):
        modified = df.groupby('iyear', as_index=False).count()
        modified = modified[(modified['iyear'] >= start) &
                            (modified['iyear'] <= end)]
        return ColumnDataSource(modified)

    def update():
        new_src = make_data(df, year.value[0], year.value[1])
        src.data.update(new_src.data)

    year.on_change('value', lambda attr, old, new: update())
    src = make_data(df)

    TOOLTIPS = [
        ("Year", "@iyear"),
        ("Counts", "@eventid")
    ]

    p = figure(plot_height=800, plot_width=800,
               title='Total attacks over years',
               x_axis_label='Years',
               y_axis_label='Attacks',
               tooltips=TOOLTIPS,
               output_backend="webgl")
    p.line(x='iyear', y='eventid', source=src, line_width=2)
    p.circle(x='iyear', y='eventid', source=src, size=8, fill_color='white')

    tab = Panel(child=row(year, p), title='Total Attacks')

    return tab
