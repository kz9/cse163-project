import pandas as pd
import geopandas
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def plot_year(shape, csv):
    year = csv.filter(items=['imonth'])
    year = year[year['imonth'] > 0]
    year = year.dropna()
    year['count'] = 1
    year = year.groupby(['imonth'])['count'].sum()

    fig, ax = plt.subplots()
    plot = year.plot(x='imonth', figsize=(10, 5))
    plt.title(label='Number of Attacks In Each Month')
    plt.xlabel('Month')
    plt.ylabel('Number of Total Attacks')

    a = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    plt.xticks(b, a, rotation='vertical')
    return plot


def plot_counts(shape_data, csv_data, year):
    count = csv_data.filter(items=['country_txt', 'iyear'])
    count = count[count['iyear'] == year]

    fig, ax = plt.subplots(figsize=(20, 6))
    shape_data.plot(ax=ax, color='#eeeeee')

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
                                   left_on='SOVEREIGNT', how='outer')
    merged_data = merged_data.dropna()
    plot = merged_data.plot(ax=ax, column='count', legend=True, cmap='YlOrRd')
    return plot


def main():
    csv_data = pd.read_csv('terrorism_filtered.csv', na_values=' ')
    path = 'ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp'
    shape_data = geopandas.read_file(path)
    shape_data = shape_data.filter(items=['SOVEREIGNT', 'geometry'])
    shape_data = shape_data[~(shape_data['SOVEREIGNT'] == 'Antarctica')]
    # a = plot_counts(shape_data, csv_data, 2000)
    # plt.show()


if __name__ == '__main__':
    main()
