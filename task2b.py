from weather import Weather
weather = Weather()

# Userdefined city
cityname=input("enter city")
location = weather.lookup_by_location(cityname)
condition = location.condition()
print (condition['text'])

#for all the days
alldays=[]

i=0
for forecasts in location.forecast():
    if i<5:
        day = []
        day.append(forecasts['text'])
        day.append(forecasts['date'])
        day.append(forecasts['high'])
        day.append(forecasts['low'])
        alldays.append(day)
        i+=1

print(alldays)
