from modules.classifier import ClaimsClassifier
from modules.load_data import load_data
import pickle

data = load_data("./data/frases.json")
X = data['reclamo']
y = data['etiqueta']

clf = ClaimsClassifier()
clf.fit(X, y)

with open('./data/claims_clf.pkl', 'wb') as file:
    pickle.dump(clf, file)
    print("Clasificador guardado en './data/claims_clf.pkl'")