# type conversions
# 1 mile = 1.609Km

miles = input('Enter distance in miles: ')
print(type(miles))
miles = float(miles)
km = miles * 1.609
print('Distance in km: ' + str(km))
# str has to be converted to float the int

