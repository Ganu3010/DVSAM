from asyncio.windows_events import NULL
import pandas as pd
class Search:
    def __init__(self):
        self.df = pd.read_csv('home\searchable.csv').fillna('n/a')
    def search(self, search_var):
        if search_var == '':
            return self.df
        search_var = search_var.split()
        output = pd.DataFrame(columns =['Restaurant_Name', 'Web_Link', 'Locality','Ratings_out_of_5', 'Cuisines', 'Charges_for_two'])
        for i in self.df.columns:
            for j in range(12188):
                for sv in search_var:
                    try:
                        if sv in self.df[i][j]:
                            output = output.append(self.df.loc[j])
                    except:
                        pass
        return output.drop_duplicates(subset = None, keep = 'first')