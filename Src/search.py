import pandas as pd
class Search:
    def __init__(self):
        self.df = pd.read_csv('searchable.csv')
    def search(self, search_var):
        search_var = search_var.split()
        output = pd.DataFrame(columns =['Restaurant_Name', 'Web_Link', 'Locality','Ratings_out_of_5', 'Cuisines', 'Charges_for_two'])
        for i in self.df.columns:
            for j in range(12188):
                for sv in search_var:
                    if sv in self.df[j][i]:
                        output = output.append(self.df.loc[j])
        return output.drop_duplicates(subset = None, keep = 'first')