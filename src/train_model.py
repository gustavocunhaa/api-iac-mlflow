from ucimlrepo import fetch_ucirepo 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from pipe.train import ExperimentMlflow

# CONSTANTES
SEED = 1337
NOME_EXPERIMENTO = "Iris Experiment"

# DATA AND EXPERIMENT TRACKING
iris = fetch_ucirepo(id=53)  
x = iris.data.features
x = x.rename(columns={
    "sepal length": "sepal_length",
    "sepal width":  "sepal_width",
    "petal length": "petal_length",
    "petal width":  "petal_width"
})
y = iris.data.targets 

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=SEED)

# EXPERIMENT RUN
infra_dev = ExperimentMlflow(nome_experimento=NOME_EXPERIMENTO)
infra_dev.run_sklearn(
    nome_run="iris_classifier",
    pipeline=RandomForestClassifier(random_state=SEED),
    X_train=x_train,
    X_test=x_test,
    y_train=y_train,
    y_test=y_test
)