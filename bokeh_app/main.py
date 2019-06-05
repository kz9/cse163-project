# Pandas for data management
import pandas as pd
import geopandas
from shapely.geometry import Point

# os methods for manipulating paths

# Bokeh basics
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs

# Each tab is drawn by one script
from scripts.total import total_tab
#from scripts.density import density_tab
#from scripts.table import table_tab
#from scripts.draw_map import map_tab
#from scripts.routes import route_tab

# Read data into dataframes
df = pd.read_pickle('database/data.pkl')

gdf = geopandas.GeoDataFrame(
        df, crs={'init': 'epsg:3395'},
        geometry=[Point(x, y) for x, y in zip(df.longitude, df.latitude)])

# create tabs
tab1 = total_tab(df)
#tab2 = dot_tab(gdf)
#tab3 = map_tab(gdf)
#tab4 = static_tab(gdf)
#tab5 = bar_tab(gdf)


# Put all the tabs into one application
tabs = Tabs(tabs=[tab1])

# Put the tabs in the current document for display
curdoc().add_root(tabs)
