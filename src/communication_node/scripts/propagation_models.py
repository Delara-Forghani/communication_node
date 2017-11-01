#!/usr/bin/env python
# coding=utf-8
"""Propagation Models.

# Authors:  Sajjad Azami <sajjadaazami@gmail.com>
#           Saman Golestannejad
# License:  BSD 3 clause

This package implements propagation model functions to compute signal strength(dBm).

Provides "Propagation Models" below
    1. One-Slope Model,
        [1] Rappaport, T.S., 1996. Wireless communications: principles and practice (Vol. 2). New Jersey: prentice hall PTR.
        [2] Zvanovec, Stanislav, Pavel Pechac, and Martin Klepal. "Wireless LAN networks design: site survey or propagation modeling?." Radioengineering 12.4 (2003): 42-49.
    2. Multi-Wall Model
    3. Rayleigh Fading Model
    4. Floor Attenuation

Using different models
----------
Setting the parameters before running the node in param.yaml
each message has parameter 'prop_model_type' that can be set.

Relations
----------
subscribes from /change_model_topic

"""

import numpy as np


# TODO get the model parameters from parameter server

def _one_slope_model_checker(distance, decay_factor, l0, threshold):
    print ("ARE THESE RIGHT??",distance, decay_factor, l0, threshold)
    signal_loss = l0 + 10 * decay_factor * np.log10(distance)
    print signal_loss

    if signal_loss <= threshold:
        return True
    else:
        return False


def _one_slope_model_strength(distance, decay_factor, l0):
    return l0 + 10 * decay_factor * np.log10(distance)


def one_slope_model_checker(distance,
                            decay_factor=4.0,
                            l0=33.3,
                            threshold=70):
    """Compute the possibility of communication using 1SM method.
        l0 and decay_factor are empirical parameters for a given environment.
        Tab.1 in [2] presents a few values taken from various references.
        Here are some recommended values:
         ------------------------------
        |  l0  |  n  |    comment      |
         ------------------------------
        | 33.3 | 4.0 |    office       |
        | 37.5 | 2.0 |    open space   |
        | 39.2 | 1.4 |    corridor     |
        | 38.5 | 3.5 | office building |
        | 38.0 | 2.0 |    passage      |
        | 38.0 | 1.3 |    corridor     |
        | 40.2 | 4.2 | office building |
        | 40.2 | 1.2 |    corridor     |
        | 40.0 | 3.5 | office building |
        | 46.4 | 3.5 | office building |
         ------------------------------
    :parameter

    decay_factor : power decay factor or path loss exponent

    distance : distance between robots

    l0 : reference loss value for the distance of 1m


    :returns:
    result : boolean indicating communication possibility
    """

    return _one_slope_model_checker(l0, decay_factor, distance, threshold)


def one_slope_model_strength(distance,
                             decay_factor=4.0,
                             l0=33.3):
    """Compute the signal strength using 1SM method.
    :parameter

    decay_factor : power decay factor or path loss exponent

    distance : distance between robots

    l0 : reference loss value for the distance of 1m


    :returns:
    result : integer indicating signal loss
    """

    return _one_slope_model_strength(l0, decay_factor, distance)
