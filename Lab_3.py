from math import radians, cos, sin, asin, sqrt
import csv
import sys
with open('GeoLiteCity-Location.csv', 'rU') as csvfile:
    # read the file as a dictionary for each row ({header : value})
    lon1=0;lat1=0;
    reader = csv.DictReader(csvfile)
    name =[]
    reader.fieldnames = 'locId', 'country', 'region', 'city', 'postalCode', 'latitude', 'longitude', 'metroCode', 'areaCode' #Adding filednames to distinguish columns
    city = raw_input('Enter the name of the city you wish to search: ')#Takes user input of the city name
    print('Hello', city)
    for row in reader:
        if(row['city']!="" and row['city']!= 'None' and row['city']!= 'city'):
            if(row['city'] == city): #If the city matches, we store the latitude and longitude for that city an compute the great circle distance accordingly
                print row['city'],row['longitude']
                lon1 = float(row['longitude'])
                lat1 = float(row['latitude'])
                break;

    for row in reader: #Haversine formula is utilized below
        if(row['city']!=city and float(row['longitude'])!= 0 and row['city']!=""): #To ensure we do not compute the great circle distance for the city itself as well
            lat2 = float(row['latitude']);lon2 = float(row['longitude'])
            lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2]) #Converting the data to radians
            dlon = lon2 - lon1 ;dlat = lat2 - lat1 
            a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
            c = 2 * asin(sqrt(a))* 6371 #In Kilometers
            if(c<1000 and (row['city'] not in name)):
                name.append(row['city'])
                print "Distance from ",row['city']," are: ", c
             
                 
        
