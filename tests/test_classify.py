import unittest

import pandas.util.testing as pdt

import recordlinkage
from recordlinkage.datasets import generate

import numpy as np
import pandas as pd

class TestClassify(unittest.TestCase):

    def test_kmeans(self):

        y, match_index = generate.simulate_features()

        train_df = y.ix[match_index].sample(500)
        train_df = train_df.append(y.ix[y.index - match_index].sample(1500))

        kmeans = recordlinkage.KMeansClassifier()
        kmeans.learn(train_df)
        kmeans.predict(y)

    def test_logistic(self):

        y, match_index = generate.simulate_features()

        train_df = y.ix[match_index].sample(500)
        train_df = train_df.append(y.ix[y.index - match_index].sample(1500))

        logis = recordlinkage.LogisticRegressionClassifier()
        logis.learn(train_df, match_index)
        logis.predict(y)

