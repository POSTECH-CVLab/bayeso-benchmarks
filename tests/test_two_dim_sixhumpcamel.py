#
# author: Jungtaek Kim (jtkim@postech.ac.kr)
# last updated: November 5, 2020
#

import numpy as np
import pytest

from benchmarks.two_dim_sixhumpcamel import *

class_fun = SixHumpCamel

TEST_EPSILON = 1e-5


def test_init():
    obj_fun = class_fun()

def test_validate_properties():
    obj_fun = class_fun()
    obj_fun.validate_properties()

def test_output():
    obj_fun = class_fun()
    bounds = obj_fun.get_bounds()

    grids = obj_fun.get_grids(3)
    truths_grids = np.array([
        [162.9],
        [48.],
        [150.9],
        [108.9],
        [0.],
        [108.9],
        [150.9],
        [48.],
        [162.9],
    ])
    
    print(grids)
    print(obj_fun.output(grids))
    print(np.abs(obj_fun.output(grids) - truths_grids) < TEST_EPSILON)
    assert np.all(np.abs(obj_fun.output(grids) - truths_grids) < TEST_EPSILON)
