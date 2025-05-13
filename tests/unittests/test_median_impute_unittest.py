
import numpy as np

from source.imputation_methods import median_impute_dynamic


def test_1d_median_impute():
    test_array=np.array([3,50.5,8,11,9,np.nan])
    expected_array=np.array([3,50.5,8,11,9,9])

    response_array= median_impute_dynamic(test_array)
    return np.testing.assert_array_equal(response_array,expected_array)



if __name__ == '__main__':
    test_1d_median_impute()
