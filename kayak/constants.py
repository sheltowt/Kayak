# Authors: Harvard Intelligent Probabilistic Systems (HIPS) Group
#          http://hips.seas.harvard.edu
#          Ryan Adams, David Duvenaud, Scott Linderman,
#          Dougal Maclaurin, Jasper Snoek, and others
# Copyright 2014, The President and Fellows of Harvard University
# Distributed under an MIT license. See license.txt file.

import numpy as np

from . import Differentiable

class Constant(Differentiable):
    __slots__ = []
    def __init__(self, val):
        super(Constant, self).__init__([])
        self.value = np.atleast_1d(val)

    def grad(self, other):
        return np.zeros(other.shape)

    def _compute_value(self):
        raise Exception("Shouldn't need this. Value should be cached")

    def _local_grad(self, parent, d_out_d_self):
        raise Exception("Shouldn't get here.")

class Parameter(Constant):
    def __init__(self, val):
        super(Parameter, self).__init__(val)
