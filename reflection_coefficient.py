# -*- coding: utf-8 -*-
"""
Script to plot reflection & transmission coefficients of EM waves.
Created on Mon Apr 18 06:51:42 2016

@author: ejetzer
"""

import numpy as np
import pylab

n_air = 1
n_glass = 1.5
n_diamond = 2.4

def alpha(n1=n_air, n2=n_glass, incident_angle=0):
    numerator_squared = 1 - ( n1 / n2 * np.sin(incident_angle) )**2
    numerator = np.sqrt(numerator_squared)
    denominator = np.cos(incident_angle)
    res = numerator / denominator
    return res

def beta(n1=n_air, n2=n_glass, mu1=1, mu2=1):
    permeabilities = mu1 / mu2
    refraction_indices = n2 / n1
    res = permeabilities * refraction_indices
    return res

def r(n1=n_air, n2=n_glass, mu1=1, mu2=1, incident_angle=0):
    a, b = alpha(n1, n2, incident_angle), beta(n1, n2, mu1, mu2)
    numerator = a - b
    denominator = a + b
    res = numerator / denominator
    return res

def t(n1=n_air, n2=n_glass, mu1=1, mu2=1, incident_angle=0):
    a, b = alpha(n1, n2, incident_angle), beta(n1, n2, mu1, mu2)
    denominator = a + b
    res = 2 / denominator
    return res

angles = np.linspace(0, np.pi/2, 100)
rs = r(n1=n_glass, n2=n_diamond, incident_angle=angles)
ts = t(n1=n_glass, n2=n_diamond, incident_angle=angles)

pylab.plot(angles, rs, label='Reflection')
pylab.plot(angles, ts, label='Transmission')
pylab.legend()
pylab.grid()
pylab.xlabel('Incident angle')
pylab.ylabel('Wave coefficient')
pylab.title('How much goes through (E//plane)?')
pylab.savefig('plot_parallel.png')
pylab.show()
