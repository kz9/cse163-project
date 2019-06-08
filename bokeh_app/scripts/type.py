from bokeh.plotting import figure
from bokeh.layouts import row, WidgetBox
from bokeh.models import Panel, ColumnDataSource, HoverTool
from bokeh.palettes import brewer
from bokeh.models.widgets import RangeSlider, CheckboxGroup


def type_tab(df):
    """
    Make a tab includes a line plot which shows how different
    attack types affected when year pass
    Parameters:
        df (DataFrame): a pandas dataframe

    Returns:
        tab: a bokeh object
    """
    # Setup needed variable
    unique_types = list(df.attacktype1_txt.unique())
    palette = brewer['Spectral'][len(unique_types)]
    colormap = {unique_types[i]: palette[i] for i in range(len(unique_types))}

    def make_data(df, start=1970, end=2017, types=unique_types):
        """
        Modify data for plotting
        Parameters:
            df (DataFrame): a pandas dataframe
            start (int): start year number
            end (int): end year number
            types (list): a list of unique attack type

        Returns:
            ColumnDataSource: a bokeh object
        """
        modified = df[(df['iyear'] >= start) &
                      (df['iyear'] <= end)].\
            groupby(['iyear', 'attacktype1_txt'], as_index=False).count()
        modified = modified[modified['attacktype1_txt'].isin(types)]
        source = {}
        for i in range(len(types)):
            if 'x' in source.keys():
                source['x'].append(list(modified[
                    modified['attacktype1_txt'] == types[i]].iyear))
                source['y'].append(list(modified[
                    modified['attacktype1_txt'] == types[i]].eventid))
                source['type'].append(list(modified[
                    modified['attacktype1_txt'] == types[i]
                    ].attacktype1_txt.unique()))
                source['colors'].append(colormap[types[i]])
            else:
                source['x'] = [list(modified[
                    modified['attacktype1_txt'] == types[i]].iyear)]
                source['y'] = [list(modified[
                    modified['attacktype1_txt'] == types[i]].eventid)]
                source['type'] = [list(modified[
                    modified['attacktype1_txt'] == types[i]
                    ].attacktype1_txt.unique())]
                source['colors'] = [colormap[types[i]]]
        return ColumnDataSource(source)

    def update():
        """
        Update the ColumnDataSource when client interact with widgets
        """
        selected_types = [types.labels[i] for i in types.active]
        new_src = make_data(df, year.value[0], year.value[1], selected_types)
        src.data.update(new_src.data)

    # Setup needed variable
    year = RangeSlider(start=1970, end=2017, value=(1970, 2017), step=1,
                       title="Year Range")
    types = CheckboxGroup(labels=unique_types,
                          active=list(range(len(unique_types))))
    src = make_data(df)
    year.on_change('value', lambda attr, old, new: update())
    types.on_change('active', lambda attr, old, new: update())
    controls = WidgetBox(year, types)

    # line plot
    p = figure(plot_height=600, plot_width=800,
               title='Attack Types',
               x_axis_label='Years',
               y_axis_label='Types',
               output_backend='webgl')
    p.multi_line(xs='x', ys='y', source=src,
                 line_color='colors', line_width=2,
                 legend='type')
    p.legend.location = 'top_left'
    p.add_tools(HoverTool(show_arrow=False, tooltips=[
        ('Year', '$data_x'),
        ('Counts', '$data_y'),
        ('Type', '@type')
    ]))

    # Setup tab structure and name
    tab = Panel(child=row(controls, p), title='Attack Types')

    return tab
