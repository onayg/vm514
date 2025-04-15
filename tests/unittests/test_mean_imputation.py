import unittest

import numpy as np


def test_mean_imputation():
    test_array = np.array([np.nan,1,3])
    expected = np.array([2,1,3])
    test_output = mean_impute(test_array)
    np.testing.assert_array_equal(test_output, expected)



if __name__ == '__main__':
    test_mean_imputation()