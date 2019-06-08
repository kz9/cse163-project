# Pandas for data management
import pandas as pd
from os.path import dirname, join

# Bokeh basics
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs

# Each tab is drawn by one script
from scripts.total import total_tab
from scripts.type import type_tab
from scripts.map import map_tab
from scripts.gif import gif_tab
from scripts.effect import effect_tab

# Read data into dataframes
df = pd.read_pickle(join(dirname(__file__), 'database', 'data.pkl'))
shp = pd.read_pickle(join(dirname(__file__), 'database', 'shp.pkl'))

# create tabs
tab1 = total_tab(df)
tab2 = type_tab(df)
tab3 = map_tab(df, shp)
tab4 = gif_tab()
tab5 = effect_tab(df)


# Put all the tabs into one application
tabs = Tabs(tabs=[tab1, tab2, tab3, tab4, tab5])

# Put the tabs in the current document for display
curdoc().add_root(tabs)
