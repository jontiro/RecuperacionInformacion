# Importar librerias
from sklearn.datasets import load_iris
import pandas as pd
import numpy
from matplotlib import pyplot
from pandas.plotting import scatter_matrix
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.feature_selection import SelectKBest, chi2, RFE
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.linear_model import LogisticRegression

# Cargar el dataset de iris
data = load_iris()
x = data.data
y = data.target
dataframe = pd.DataFrame(x, columns=data.feature_names)
dataframe['clase'] = y
# Impresion para debug
print(dataframe.head())

# Visualizacion
correlations = dataframe.corr()
names = dataframe.columns
fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin = -1, vmax = 1)
fig.colorbar(cax)
ticks = numpy.arange(0,len(names),1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names, rotation=45)
ax.set_yticklabels(names)
pyplot.show()

# Attrib selection
print("=" * 40)
print("Attrib selection")
print("=" * 40)
test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(x, y)
set_printoptions(precision = 3)
print(fit.scores_)
features = fit.transform(x)
print(features[0:5, :])

# Feature importance
model = ExtraTreesClassifier(n_estimators=100)
model.fit(x, y)
print()
print("=" * 40)
print("Feature importance")
print("=" * 40)
print(model.feature_importances_)

# Feature Extraction
model_RFE = LogisticRegression(max_iter = 1000)
rfe = RFE(estimator=model_RFE, n_features_to_select = 4)
rfe.fit(x, y)
print()
print("=" * 40)
print("Feature Extraction (RFE)")
print("=" * 40)
print("Num Features: %d" % fit.n_features_)
print("Selected features: %s" % fit.support_)
print("Feature Ranking: %s" % fit.ranking_)