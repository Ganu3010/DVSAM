import numpy as np
from final import Predicting
import pandas as pd
x = Predicting()

combined = pd.read_csv('G:/Projects/DVSAM/Src/combined.csv')

user1 = {}
ls = [combined['rest_name'][0], combined['rest_name'][10], combined['rest_name'][20]]

print(type(ls[0]))

# user1[ls[0]: 3, ls[1]: 4, ls[2]: 2]
user1[ls[0]] = 3
user1[ls[1]] = 4
user1[ls[2]] = 2
# t = x.get_restaurant(user1)
sim_rest = pd.DataFrame()
m = np.array(list(user1.values())).mean()
for rest in user1:
    print(rest, user1[rest])
