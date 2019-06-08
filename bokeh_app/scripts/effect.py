from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.models import Panel, ColumnDataSource
from bokeh.models.widgets import Slider


def effect_tab(df):
    """
    This will create a tab which show the relationship between
    year and Attack counts
    Parameters:
        df (DadaFrame): a pandas dataframe

    Returns:
        tab: bokeh object
    """
    # Setup needed variable
    abb = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'July',
           'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']

    def make_data(df, year=1970, month=abb):
        """
        Modify the dataframe for plotting
        Parameter:
            df (DataFrame): a pandas dataframe
            month (list): a list of month abbreviated
            year (int): specific year passed by client,
                        default value 1970

        Returns:
            ColumnDataSource: a bokeh object like dataframe
        """
        modified = df[df['iyear'] == year].groupby(
                'imonth', as_index=False)['eventid'].count()
        modified = modified[modified['imonth'] != 0]
        abb = []
        for i in list(modified['imonth']):
            abb.append(month[i - 1])
        modified['months'] = abb
        return ColumnDataSource(modified)

    def make_static_data(df, month=abb):
        """
        Modify the dataframe for plotting
        Parameter:
            df (Dataframe): a pandas dataframe
            month (list): a list of month abbreviated

        Returns:
            ColumnDataSource: a bokeh object
        """
        modified = df.groupby(
                'imonth', as_index=False)['eventid'].count()
        modified = modified[modified['imonth'] != 0]
        abb = []
        for i in list(modified['imonth']):
            abb.append(month[i - 1])
        modified['months'] = abb
        return ColumnDataSource(modified)

    def update():
        """
        update the dataframe when client interact with slider
        """
        new_src = make_data(df, year.value)
        src.data.update(new_src.data)

    # Setup nessary value
    year = Slider(start=1970, end=2017, value=1970, step=1,
                  title="Year Range")
    year.on_change('value', lambda attr, old, new: update())
    src = make_data(df)
    static = make_static_data(df)

    # Hover information
    TOOLTIPS = [
        ('Month', '@months'),
        ('Counts', '@eventid')
    ]

    # Plot one show relationship between attack numbers and each year
    p1 = figure(plot_height=600, plot_width=800,
                title='Total Attacks Over Different Year by Month',
                x_axis_label='Month',
                y_axis_label='Attacks',
                tooltips=TOOLTIPS,
                output_backend="webgl")
    p1.line(x='imonth', y='eventid', source=src, line_width=2, color='red')
    p1.circle(x='imonth', y='eventid', source=src, size=8, fill_color='white')

    # Plot two show relationship between attack numbers and each month
    p2 = figure(plot_height=600, plot_width=800,
                title='Total Attacks Over Years by Month',
                x_axis_label='Month',
                y_axis_label='Attacks',
                tooltips=TOOLTIPS,
                output_backend="webgl")
    p2.line(x='imonth', y='eventid', source=static, line_width=2, color='blue')
    p2.circle(x='imonth', y='eventid', source=static, size=8,
              fill_color='white')

    # Setup tab name and structure
    tab = Panel(child=column(year, p1, p2),
                title='Year Effect Attacks')

    return tab
