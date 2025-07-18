# tee ratkaisu tänne
# Write your solution here

# reads the names and the locations of all the stations in the file and returns them in a dictionary
def get_station_data(filename: str):
    raw_station_list = []
    station_dict = {}

    with open(filename) as new_file:
        for row in new_file:
            row = row.strip()
            row = row.split(";")
            # it appears to automatically add the row as a list
            raw_station_list.append(row)
    
    for row in raw_station_list:
        # don't want the first row that contains the labels
        if row == raw_station_list[0]:
            continue
        # convert the longitudes and the latitudes to float
        longitude = float(row[0])
        latitude = float(row[1])
        name = row[3]
        station_dict[name] = (longitude, latitude)
    
    return station_dict

# calculate distance between two stations
def distance(stations: str, station1: str, station2: str):
    # first pull out longitudes and latitudes for the two stations
    longitude1 = stations[station1][0]
    longitude2 = stations[station2][0]
    latitude1 = stations[station1][1]
    latitude2 = stations[station2][1]
    # use the pythagorean theorem to calculate distance
    import math
    
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

# find the greatest distance between two stations, return the stations and the distance
def greatest_distance(stations: dict):
    longest = 0
    greatest_station1 = ""
    greatest_station2 = ""
    for key1 in stations:
        for key2 in stations:
            current_dist = distance(stations, key1, key2)
            if current_dist > longest:
                longest = current_dist
                greatest_station1 = key1
                greatest_station2 = key2
    return (greatest_station1, greatest_station2, longest)

if __name__ == "__main__":
    stations = get_station_data('src/stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)

    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)