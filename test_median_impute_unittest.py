
import unittest
import numpy as np

def median_impute_dynamic(arr):
    if not isinstance(arr, np.ndarray):
        raise ValueError("Input must be a numpy ndarray.")
    if np.isnan(arr).all():
        raise ValueError("Array contains only NaN values.")

    if arr.ndim == 1:
        median = np.nanmedian(arr)
        return np.where(np.isnan(arr), median, arr)

    elif arr.ndim == 2:
        imputed = arr.copy()
        for i in range(arr.shape[1]):
            col = arr[:, i]
            median = np.nanmedian(col)
            imputed[:, i] = np.where(np.isnan(col), median, col)
        return imputed

    elif arr.ndim == 3:
        imputed = arr.copy()
        for i in range(arr.shape[2]):
            slice_ = arr[:, :, i]
            median = np.nanmedian(slice_)
            imputed[:, :, i] = np.where(np.isnan(slice_), median, slice_)
        return imputed

    else:
        raise ValueError("Only 1D, 2D or 3D arrays are supported.")

if __name__ == '__main__':
    unittest.main()
