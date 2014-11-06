import os
import shapefile
import Settings
from scipy import spatial
from matplotlib.path import Path

class Shape():
    def __init__(self, filename):
        self.sf = None
        self.search_tree = None
        filepath = os.path.join(Settings.STATIC_PATH, filename)
        self.readShape(filepath)

    def readShape(self, filepath):
        self.sf = shapefile.Reader(filepath)
        self.buildSearchTree()

    def buildSearchTree(self):
        records = self.sf.records()
        latlngs = []
        for r in records:
            latlngs.append((float(r[-2]), float(r[-1])))
        self.search_tree = spatial.KDTree(latlngs)

    def searchZip(self, lat, lng):
        if self.search_tree != None:
            query_latlng = (float(lat), float(lng))
            results = self.search_tree.query(query_latlng, 10)
            results = zip(*results)
            inside = False
            for r in results:
                zipcode = self.sf.record(r[1])[0]
                points = self.sf.shape(r[1]).points
                p = Path(points)
                inside = p.contains_points([[float(lng), float(lat)]])
                if inside == True:
                    break
            if inside == True:
                print "Found ZIP: " + zipcode
                return (zipcode, points)
            else:
                print "Not Found..."
                return ("None", [])