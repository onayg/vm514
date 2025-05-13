import unittest
import pandas as pd

from source.imputation_methods import mean_impute


class TestMeanImputation(unittest.TestCase):
    def test_mean_imputation(self):
       data = {
            'A': [1.0, 2.0, None, 4.0, 5.0],
            'B': [7.0, None, 9.0, 10.0, 11.0]
        }
       df = pd.DataFrame(data)

       expected_data = {
            'A': [1.0, 2.0, 3.0, 4.0, 5.0],         
            'B': [7.0, 9.25, 9.0, 10.0, 11.0]       
        }
       expected_df = pd.DataFrame(expected_data)

       result_df = mean_impute(df)

        
       pd.testing.assert_frame_equal(result_df, expected_df)


if __name__ == '__main__':
    unittest.main()