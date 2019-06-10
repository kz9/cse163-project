# This file is used to plot the number of attacks for each country in the world
# for each year. The plots are saved as PNGs and used as frames to create a
# GIF in Photoshop.

import pandas as pd
import geopandas
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")


def plot_counts(shape_data, csv_data, year):
    """
    Is passed a shape file, a csv, and a year. Creates a plot for that specific
    year that shows the relative number of attacks in each country. Saves the
    plot as a png to a folder named "frames". (Requires a folder with that name
    to be created in the same directory).
    """
    count = csv_data.filter(items=['country_txt', 'iyear'])
    count = count[count['iyear'] == year]

    fig, ax = plt.subplots(figsize=(60, 20))

    # Plots entire world first in gray as a background, to display a country
    # with no attacks for that year as gray
    shape_data.plot(ax=ax, color='#eeeeee')

    # Shape file and csv file had differences in country names, so it required
    # some name changes. If the locations/borders of some countries were
    # different at different points in time, the country with the closest
    # political and geograpical analog was used (ex: West and East Germany
    # changed to Germany).
    count = count.replace(['Czechia', 'East Germany (GDR)', 'Serbia',
                           'Slovak Republic', 'Bahamas', 'Tanzania',
                           'United States', 'West Bank and Gaza Strip',
                           'West Germany (FRG)'],
                          ['Czech Republic', 'Germany', 'Republic of Serbia',
                           'Slovakia', 'The Bahamas',
                           'United Republic of Tanzania',
                           'United States of America', 'Israel', 'Germany'])
    count = count.dropna()
    count['count'] = 1

    count = count.groupby('country_txt')['count'].sum()
    merged_data = shape_data.merge(count, right_on='country_txt',
                                   left_on='SOVEREIGNT', how='outer',
                                   sort=True)
    merged_data = merged_data.dropna()

    merged_data.plot(ax=ax, column='count', legend=False, cmap='YlOrRd')
    plt.axis('off')
    plt.text(0.05, 0.2, year, transform=ax.transAxes, fontsize=25)
    plt.savefig('frames/' + str(year) + '.png')


def main():
    csv_data = pd.read_csv('terrorism_filtered.csv', na_values=' ')
    path = 'ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp'
    shape_data = geopandas.read_file(path)
    shape_data = shape_data.filter(items=['SOVEREIGNT', 'geometry'])
    shape_data = shape_data[~(shape_data['SOVEREIGNT'] == 'Antarctica')]
    # Loop to plot every year (except 1993, reasons discussed in report).
    for i in range(1970, 2018):
        if i != 1993:
            plot_counts(shape_data, csv_data, i)


if __name__ == '__main__':
    main()
