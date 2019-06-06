import pandas as pd
import hvplot.pandas
import pandas_bokeh
from bokeh.plotting import figure
from bokeh.layouts import column, row, WidgetBox
from bokeh.models import Panel, ColumnDataSource, HoverTool
from bokeh.palettes import brewer, Spectral6, inferno
from bokeh.transform import factor_cmap
from bokeh.models.tools import CustomJSHover
from bokeh.models.widgets import RangeSlider, CheckboxGroup


def map_tab(gdf):
    unique_types = list(df.attacktype1_txt.unique())
    palette = brewer['Spectral'][len(unique_types)]
    colormap = {unique_types[i]: palette[i] for i in range(len(unique_types))}

    def make_data(df, start=1970, end=2017, types=unique_types):
        modified = gdf[(gdf['iyear'] >= start) &
                      (gdf['iyear'] <= end)].\
            groupby(['iyear', 'attacktype1_txt'], as_index=False).count()
        modified = modified[modified['attacktype1_txt'].isin(types)]
               return ColumnDataSource(source)

    def update():
        selected_types = [types.labels[i] for i in types.active]
        new_src = make_data(df, year.value[0], year.value[1], selected_types)
        src.data.update(new_src.data)

    year = RangeSlider(start=1970, end=2017, value=(1970, 2017), step=1,
                       title="Year Range")
    types = CheckboxGroup(labels=unique_types,
                          active=list(range(len(unique_types))))
    src = make_data(df)

    p = figure(plot_height=800, plot_width=800,
               title='Attack Types Distrubuted Over Year',
               x_axis_label='Years',
               y_axis_label='Types',
               output_backend='webgl')
    p.multi_line(xs='x', ys='y', source=src,
                 line_color='colors', line_width=2,
                 legend='type')

    p.add_tools(HoverTool(show_arrow=False, tooltips=[
        ('Year', '$data_x'),
        ('Counts', '$data_y'),
        ('Type', '@type')
    ]))

    year.on_change('value', lambda attr, old, new: update())
    types.on_change('active', lambda attr, old, new: update())
    controls = WidgetBox(year, types)

    tab = Panel(child=row(controls, p), title='Attack Types')

    return tab
