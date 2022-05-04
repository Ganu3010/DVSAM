from final import Predicting

x = Predicting()

user1 = {'Southern Spice': 3, 'Bangalore Iyangar Bakery': 5, 'Hotel Samarth': 2}

t = x.get_restaurant(user1)


for i in t:
    print(i, ':', t[i])