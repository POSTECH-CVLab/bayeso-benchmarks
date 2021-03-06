#
# author: Jungtaek Kim (jtkim@postech.ac.kr)
# last updated: November 5, 2020
#

import numpy as np
import pytest

from benchmarks.two_dim_branin import *
from benchmarks.two_dim_eggholder import *
from benchmarks.two_dim_michalewicz import *

TEST_EPSILON = 1e-5


def test_global_minimum_branin():
    class_fun = Branin

    obj_fun = class_fun()
    grids = obj_fun.get_grids(100)
    vals_grids = obj_fun.output(grids)
    ind_minimum = np.argmin(vals_grids)
    global_minimum_brute_force = np.min(vals_grids)

    print(global_minimum_brute_force)
    print(grids[ind_minimum])
    print(obj_fun.global_minimum - global_minimum_brute_force)
    assert (obj_fun.global_minimum - global_minimum_brute_force) < TEST_EPSILON

def test_global_minimum_eggholder():
    class_fun = Eggholder

    obj_fun = class_fun()
    grids = obj_fun.get_grids(100)
    vals_grids = obj_fun.output(grids)
    ind_minimum = np.argmin(vals_grids)
    global_minimum_brute_force = np.min(vals_grids)

    print(global_minimum_brute_force)
    print(grids[ind_minimum])
    print(obj_fun.global_minimum - global_minimum_brute_force)
    assert (obj_fun.global_minimum - global_minimum_brute_force) < TEST_EPSILON

def test_global_minimum_michalewicz():
    class_fun = Michalewicz

    obj_fun = class_fun()
    grids = obj_fun.get_grids(100)
    vals_grids = obj_fun.output(grids)
    ind_minimum = np.argmin(vals_grids)
    global_minimum_brute_force = np.min(vals_grids)

    print(global_minimum_brute_force)
    print(grids[ind_minimum])
    print(obj_fun.global_minimum - global_minimum_brute_force)
    assert (obj_fun.global_minimum - global_minimum_brute_force) < TEST_EPSILON
