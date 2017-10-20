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
#days which has highest temp
max=0
for day in alldays:
    if int(day[2])>int(max):
        max=day[2]
        spotday = day[1]
print("The hottest day is and temp is max on,",spotday,max)
#for low temp
low=0
for day in alldays:
    if int(day[3])<int(low):
        low=day[3]
        spotday=day[1]
print("The coldest day is and temp is on,",spotday,low)




