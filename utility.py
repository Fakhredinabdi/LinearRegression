
class Utility:
         
    def insert_one_to_list(X):
        X = X.tolist()
        for i in range(len(X)):
            transform = X[i]
            transform.insert(0 , 1)
        return X