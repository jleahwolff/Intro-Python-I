# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon, **kw):
        self.lat = lat
        self.lon = lon
        super().__init__(**kw)
    def desc(self):
        return f'lat is {self.lat} and lon is {self.lon}'

myLocation = LatLon(23, 22)
print(myLocation.desc())

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypt(LatLon):
    def __init__(self, name, **kw):
        self.name = name
        super().__init__(**kw)

    def __str__(self):
        return f'My information: {self.name}, {self.lat}, {self.lon}'
    
    def myname(self):
        return f'My name is {self.name}'

way = Waypt('Jess', lat=20, lon=120)

print(way)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypt):
    def __init__(self, difficulty, hint, size, **kw):
        self.difficulty = difficulty
        self.size = size
        self.hint = hint
        super().__init__(**kw)

    def vDiff(self):
        return f'The Geocache is {self.difficulty} to find, size of the geocache is {self.size}, the lat is {self.lat}, long is {self.lon}. Message from the GeoTagger: {self.hint}'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

Catacombs = Geocache(lat=41.021, lon=-121.5121, name="Catacombs", size='1 inch by 2 inches', difficulty='very difficult', hint="Good luck hunters. Remember, every one of you possess a third eye shakra. You have to unlock it to find the cache.")
print(Catacombs.vDiff())

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
# print(geocache)
