import pandas as pd
import geopandas
import matplotlib
matplotlib.use("TkAgg")


# def plot_total_counts(shape_data, csv_data):
#     count = csv_data.filter(items=['country_txt'])
#     count = count.dropna()
#     count['count'] = 1
#     count = count.groupby('country_txt')['count'].sum()

#     merged_data = shape_data.merge(count, right_on='country_txt',
#                                    left_on='SOVEREIGNT', how='outer')

#     merged_data.plot(column='count', legend=True, figsize=(20, 7))
#     plt.savefig('1.png')


def plot_counts(shape_data, csv_data, year):
    count = csv_data.filter(items=['country_txt', 'iyear'])
    count = count[count['iyear'] == year]
    count = count.dropna()
    count['count'] = 1
    count = count.groupby('country_txt')['count'].sum()
    merged_data = shape_data.merge(count, right_on='country_txt',
                                   left_on='SOVEREIGNT', how='outer')

    plot = merged_data.plot(column='count', legend=True, figsize=(20, 7))
    plt.show()
    return plot


def main():
    csv_data = pd.read_csv('terrorism_filtered.csv', na_values=' ')
    path = 'ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp'
    shape_data = geopandas.read_file(path)
    shape_data = shape_data.filter(items=['SOVEREIGNT', 'geometry'])
    shape_data = shape_data[~(shape_data['SOVEREIGNT'] == 'Antarctica')]
    plot_counts(shape_data, csv_data, 2000)


if __name__ == '__main__':
    main()
