# substitute for excel data
arr0 = [5, 6, 7]
arr1 = [6, 7, 8]
arr2 = [7, 8, 9]
cities = {
    "x_county": arr0,
    "y_county": arr1,
    "z_county": arr2
}

"""
The dictionary that stores the metro county names (keys) and the associated data (values)
Format:
    Metro: Residence, Commuter Flow, Margin of Error
"""
new_cities = {}

# we will loop through the data and insert the work county name as the key
# and an array of the field listed above as the value
for x in cities:
    a = cities[x]
    new_cities[x] = a

print(new_cities)
