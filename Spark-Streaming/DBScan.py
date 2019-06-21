from math import radians, cos, sin, asin, sqrt

from scipy.spatial.distance import pdist, squareform
from sklearn.cluster import DBSCAN

import matplotlib.pyplot as plt
import csv as csv


def printing_the_distance():

    with open("/home/raxit/Desktop/location_data.csv") as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile, delimiter=';')

        for row in reader:
            print(row[0], row[1], row[2], row[3], "distance:", haversine(
                float(row[0]), float(row[1]), float(row[2]), float(row[3])))


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r


if __name__ == "__main__":
    printing_the_distance()

# X = pd.read_csv('~/Desktop/location_data.csv')
# print(X)
# distance_matrix = squareform(pdist(X, (lambda u,v: haversine(u,v))))

# db = DBSCAN(eps=0.2, min_samples=2, metric='precomputed')  # using "precomputed" as recommended by @Anony-Mousse
# y_db = db.fit_predict(distance_matrix)

# print(y_db)
# X['cluster'] = y_db

# plt.scatter(X['lat'], X['lng'], c=X['cluster'])
# plt.show()
