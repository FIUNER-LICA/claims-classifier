# Claims Classifier

Clasificador para Sistema de Gestión de Reclamos en la facultad

El objetivo de este proyecto es proveer un clasificador de reclamos entrenado guardado en el archivo pickle "claims_clf.pkl".

### Versión de Python
- Python 3.13.X (ejemplo 3.13.9)

### Dependencias necesarias

- [Scikit-learn](https://pypi.org/project/scikit-learn/): `pip install scikit-learn` 
- [spaCy](https://pypi.org/project/spacy/): `pip install spacy`  
- [Numpy](https://pypi.org/project/numpy/):`pip install numpy`
- [Pandas](https://pypi.org/project/pandas/): `pip install pandas`

### Pasos para usar el clasificador 

1 - Clonar el repositorio.

2 - Instalar las dependencias necesarias en el proyecto donde utilizarás el clasificador. En el archivo de requerimientos (/deps/requirements.txt) encontrarás las dependencias necesarias.

3 - Copiar los archivos `text_vectorizer.py` y `classifier.py` en la carpeta `modules`de tu proyecto y el archivo `claims_clf.pkl` en la carpeta `data`. 

4- Para cargar el clasificador desde el archivo y empezar a clasificar tus reclamos, seguir el ejemplo del archivo `eval_claims_clf.py` en la carpeta `apps`.

Las etiquetas que devuelve el clasificador son: `soporte informático`, `secretaría técnica` y `maestranza`.
