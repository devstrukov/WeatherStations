class WeatherStation:
    def __init__(self, guid, name, lat, lng, temperature, humidity, wind_speed):
        self.guid = guid
        self.name = name
        self.lat = lat
        self.lng = lng
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed

    def toDict(self):
        return {
            "guid": self.guid,
            "name": self.name,
            "lat": self.lat,
            "lng": self.lng,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "wind_speed": self.wind_speed,
        }