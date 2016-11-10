#! /usr/bin/env python
import os
import pymt.components


dakota_methods = ('CenteredParameterStudy', 'PolynomialChaos',
                  'StochasticCollocation', 'MultidimParameterStudy',
                  'Sampling', 'VectorParameterStudy')


os.mkdir('_testing')
os.chdir('_testing')

for method in dakota_methods:
    Model = getattr(pymt.components, method)

    model = Model()

    for default in model.defaults:
        print('{name}: {val} {units}'.format(
            name=default[0], val=default[1][0], units=default[1][1]))
