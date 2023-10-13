# c_dataframe 의 all_data_sub_by_mean_value, all_data_div_by_mean_value, all_data_mul_by_mean_value 함수를
# 테스트하는 코드를 작성해보겠습니다. 

import unittest
import pandas as pd
import numpy as np
from c_dataframe.analysis_dataframe import all_data_sub_by_mean_value, all_data_div_by_mean_value, all_data_mul_by_mean_value
from c_dataframe.analysis_dataframe import change_some_values_to_nan, change_some_values_to_null, fill_nan_null_value

class TestAnalysisDataFrame(unittest.TestCase) :
        
        def setUp(self) : 
            # 테스트를 위한 데이터 프레임 생성, 100행 10열, 값은 1부터 순차적으로 증가
            self.df = pd.DataFrame(np.arange(1,1001).reshape(100,10))
            self.df = change_some_values_to_nan(self.df)
            self.df = change_some_values_to_null(self.df)
            
        def test_all_data_sub_by_mean_value(self) : 
            df = all_data_sub_by_mean_value(self.df)
            self.assertEqual(df.shape, (100,10))
            
        def test_all_data_div_by_mean_value(self) : 
            df = all_data_div_by_mean_value(self.df)
            self.assertEqual(df.shape, (100,10))
            
        def test_all_data_mul_by_mean_value(self) : 
            df = all_data_mul_by_mean_value(self.df)
            self.assertEqual(df.shape, (100,10))
        
        # self.df 안에 nan값이 있는지 확인하는 테스트 코드입니다.
        # nan값이 있을 경우, 오류를 내고, nan값이 없을 경우, 오류를 내지 않습니다.
        
        def test_self_df_isnan(self) :
            self.assertFalse(self.df.isnull().values.any())
        
        def test_self_df_isnull(self) :
            self.assertFalse(self.df.isna().values.any())
            
        # fill nan null value 함수를 테스트하는 코드입니다.
        # nan값을 가지고 있는 데이터 프레임을 넣어서 nan값을 0으로 변경하고,
        # 빈값을 가지고 있는 데이터 프레임을 넣어서 빈값을 0으로 변경합니다.
        # 이후에 nan값이나 빈값이 있는지를 확인합니다.
        
        def test_fill_nan_null_value(self) :
            df = fill_nan_null_value(self.df)
            self.assertFalse(df.isnull().values.any())
            self.assertFalse(df.isna().values.any())
            
            
            
        # 현재 테스트된 함수들은 nan값을 가지고 있을 경우, 오류를 내지 않고 그냥 계산하고 있습니다. 
        # 테스트 결과를 토대로 nan값을 가지고 있을 경우, 처리하도록 코드를 수정해야 합니다.
        # 원래는 본소스를 수정해야하지만 금일은 쉽게 처리하기 위해 처리함수를 추가하겠습니다.
        
        def test_all_data_sub_by_mean_value_isnan_with_fillna(self) : 
            df = fill_nan_null_value(self.df)
            df = all_data_sub_by_mean_value(df)
            self.assertFalse(df.isnull().values.any())
            
        def test_all_data_div_by_mean_value_isnan_with_fillna(self) :
            df = fill_nan_null_value(self.df)
            df = all_data_div_by_mean_value(df)
            self.assertFalse(df.isnull().values.any())
            
        def test_all_data_mul_by_mean_value_isnan_with_fillna(self) :
            df = fill_nan_null_value(self.df)
            df = all_data_mul_by_mean_value(df)
            self.assertFalse(df.isnull().values.any())
            

        
            