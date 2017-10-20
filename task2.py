from weather import Weather
weather = Weather
cityname=input("enter city")
location = weather.lookup_by_location(cityname)
condition = location.condition()
print condition['text']
