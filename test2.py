
from sklearn.datasets import load_iris 
from sklearn.model_selection import KFold,cross_val_score 


data = load_iris() 
X = data.data
y = data.target 

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

fold = KFold(n_splits=5) 

res = cross_val_score(model,X,y,cv=fold)
print(f"accuracy: : {res}")