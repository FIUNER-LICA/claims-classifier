import json
import pandas as pd


def load_data(p_path):
    """
    Carga datos desde un archivo JSON y los convierte en un DataFrame de pandas.
    """
    with open(p_path,'r', encoding='utf-8') as f:
        training_data = json.load(f)

    claims = [None for _ in range(len(training_data))]
    labels = claims.copy()

    i = 0
    for registry in training_data: 
        claims[i] = registry['reclamo']
        labels[i] = registry['etiqueta']
        i += 1
        
    return pd.DataFrame({'reclamo':claims, 'etiqueta':labels})
  
  
if __name__ == "__main__":
    data = load_data("./data/frases.json")
    print(data)