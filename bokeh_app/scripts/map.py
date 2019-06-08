import pandas as pd
import pandas_bokeh
from bokeh.layouts import row
from bokeh.models import Panel


def map_tab(df, shp):
    """
    Make a tab wich contains a map colored by the number of
    terrorism attacks
    Parameters:
        df (DataFrame): a pandas dataframe
        shp (GeoDataFrame): a geopandas dataframe

    Returns:
        tab: a bokeh object
    """
    def make_data(df, shp, start=1970, end=2017):
        """
        Modify data for plotting
        Parameters:
            df (DataFrame): a pandas dataframe
            shp (GeoDataFrame): a geopandas dataframe
            start (int): start year number
            end (int): end year number

        Returns:
            GeoDataFrame: contains map data
        """
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

    # Setup needed variable
    src = make_data(df, shp)
    slider_columns = ['year_{}'.format(i) for i in range(1970, 2018)]
    srange = range(1970, 2018)

    # Map plot
    p = src.plot_bokeh(
        figsize=(900, 600),
        simplify_shapes=5000,
        slider=slider_columns,
        slider_range=srange,
        slider_name="Year",
        colormap='Viridis',
        hovertool_columns=['country_txt'],
        title="Cumulative Attacks Map")

    # Setup tab structure and name
    tab = Panel(child=row(p), title='Cumulative Map')

    return tab
