# Copyright 2019 Seth V. Neel, Michael J. Kearns, Aaron L. Roth, Zhiwei Steven Wu
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

import numpy as np
import pdb

class RegOracle:
    """Class using regression oracle to solve CSC problem."""
    def __init__(self, b0, b1):
        self.b0 = b0
        self.b1 = b1

    def predict(self, X):
        """Predict labels on data set X."""
        reg0 = self.b0
        reg1 = self.b1
        n = X.shape[0]
        y = []
        pdb.set_trace()
        for i in range(n):
            x_i = X.iloc[i, :]
            x_i = x_i.values.reshape(1, -1)
            c_0 = reg0.predict(x_i)
            c_1 = reg1.predict(x_i)
            y_i = int(c_1 < c_0)
            y.append(y_i)
        return y


class RandomLinearThresh:
    """Class random hyperplane classifier, used in experiments."""
    def __init__(self, d):
        self.coefficient = [np.random.uniform(-1, 1) for _ in range(d)]

    def predict(self, X):
        """Predict labels on data set X."""
        beta = self.coefficient
        n = X.shape[0]
        y = []
        for i in range(n):
            x_i = X.iloc[i, :]
            c_1 = np.dot(beta, x_i)
            y_i = int(c_1 < 0)
            y.append(y_i)
        return y


class LinearThresh:
    """Class hyperplane classifier."""
    def __init__(self, d):
        self.coefficient = d

    def predict(self, X):
        """Predict labels on data set X."""
        beta = self.coefficient
        n = X.shape[0]
        y = []
        for i in range(n):
            x_i = X.iloc[i, :]
            c_1 = np.dot(beta, x_i)
            y_i = int(c_1 < 0)
            y.append(y_i)
        return y
