from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.models import Panel
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import RangeSlider


def total_tab(df):
    """
    Make a tab contains a line plot which is the
    total attacks number in different year
    Parameters:
        df (DataFrame): a pandas dataframe

    Returns:
        tab: a bokeh object
    """
    def make_data(df, start=1970, end=2017):
        """
        Modify data for plotting
        Parameters:
            df (DataFrame): a pandas dataframe
            start (int): start year number
            end (int): end year number

        Returns:
            ColumnDataSource: a bokeh object
        """
        modified = df.groupby('iyear', as_index=False).count()
        modified = modified[(modified['iyear'] >= start) &
                            (modified['iyear'] <= end)]
        return ColumnDataSource(modified)

    def update():
        """
        This will update the ColumnDataSource when client
        interact with the widgets
        """
        new_src = make_data(df, year.value[0], year.value[1])
        src.data.update(new_src.data)

    # Setup needed variables
    year = RangeSlider(start=1970, end=2017, value=(1970, 2017), step=1,
                       title="Year Range")
    year.on_change('value', lambda attr, old, new: update())
    src = make_data(df)

    # Hover information setup
    TOOLTIPS = [
        ("Year", "@iyear"),
        ("Counts", "@eventid")
    ]

    # line plot
    p = figure(plot_height=600, plot_width=800,
               title='Total Attacks Over the Years',
               x_axis_label='Years',
               y_axis_label='Attacks',
               tooltips=TOOLTIPS,
               output_backend="webgl")
    p.line(x='iyear', y='eventid', source=src, line_width=2)
    p.circle(x='iyear', y='eventid', source=src, size=8, fill_color='white')

    # Setup tab structure and name
    tab = Panel(child=row(year, p), title='Total Attacks')

    return tab
