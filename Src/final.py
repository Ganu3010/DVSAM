import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity  


class Predicting:
    def __init__(self):
        
        self.combine = pd.read_csv('G:/Projects/DVSAM/Src/combined.csv')
        self.combine = self.combine[['user_id', 'rest_name', 'rating']]
        self.pivot = self.combine.pivot_table(index=['user_id'], columns=['rest_name'], values='rating')
        self.pivot = self.pivot.fillna(0)
        self.pt_stand = self.pivot.apply(self.standardize)
        self.item_sim = cosine_similarity(self.pt_stand.T)
        self.item_sim = pd.DataFrame(self.item_sim, index=self.pt_stand.columns, columns=self.pt_stand.columns)

    def get_sim(self, rest, rating, mean):
        sim_score = self.item_sim[rest]*(rating)
        sim_score = sim_score.sort_values(ascending = False).head(10)
        return sim_score
    def get_restaurant(self, user_dict):
        sim_rest = pd.DataFrame()
        m = np.array(list(user_dict.values())).mean()
        for rest in user_dict:
            sim_rest = sim_rest.append(self.get_sim(rest=rest, rating = user_dict[rest], mean = m), ignore_index = True)
        
        sim_rest = sim_rest.sum().sort_values(ascending = False)
        sim_rest = dict(sim_rest.head(len(user_dict) + 10))
        r = {}
        for i in sim_rest:
            if not i in user_dict:
                r[i] = sim_rest[i]
        return r
    def standardize(self, row):
        if(row.max()-row.min() != 0):
            new_row = (row - row.mean())/(row.max() - row.min())
        else:
            new_row = row
        return new_row

    
        

x = Predicting()

user1 = {}
# user1['Southern Spice'] = 3
# user1['Cafe Little Eggs'] = 4
# user1['BACKSTAGE'] = 3
user1[x.combine['rest_name'][3]] = 3
user1[x.combine['rest_name'][3]] = 4
t = x.get_restaurant(user1)

for i in t:
    print(t[i])
