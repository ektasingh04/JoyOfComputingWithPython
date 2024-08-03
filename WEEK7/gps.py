import csv
from gmplot import gmplot

gmap=gmplot.GoogleMapPlotter(28.79865,77.562772,17)
gmap.coloricon="https://www.googlemapsmarkers.com/v1/%s/"


with open('route.csv','r')as f:
    reader=csv.reader(f)  #create an iterator to read over the file csv
    k=0
    for row in reader:
        lat=float(row[0])
        long=float(row[1])
        #print(lat)
        #print(long)
        #print(lat+long)
        if(k==0):
            gmap.marker(lat,long,'yellow')
            k=1
        else:
            gmap.marker(lat,long,'blue')
gmap.marker(lat,long,'red')
gmap.draw("mymap.html")