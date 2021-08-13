import math

class CityDistance:
    r = 6373.0

    def distance(self, lat1, long1, lat2, long2):
        lat1 =  float(lat1.split(" ")[0])
        long1 = float(long1.split(" ")[0])

        lat2 = float(lat2.split(" ")[0])
        long2 = float(long2.split(" ")[0])

        lat1 = math.radians(lat1)
        long1 = math.radians(long1)

        lat2 = math.radians(lat2)
        long2 = math.radians(long2)

        lat_diff = lat2 - lat1
        long_diff = long2 - long1

        a = math.sin(lat_diff / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(long_diff / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = self.r * c

        return round(distance, 2)


loc1 = input("City 1: ")
loc2 = input("City 2: ")
loc1 = loc1.split(",")
loc2 = loc2.split(",")

d = CityDistance()

distance = d.distance(loc1[0].strip(), loc1[1].strip(), loc2[0].strip(), loc2[1].strip())

print(f'City 1 and City 2 are {distance} km apart')

