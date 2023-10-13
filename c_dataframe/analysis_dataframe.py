import pandas as pd
import numpy as np

# 1. 각 컬럼의 평균값을 구한뒤, 그 평균값으로 각 컬럼의 값을 뺀다.
def all_data_sub_by_mean_value(df) :
    df_mean = df.mean()
    df_sub = df.sub(df_mean, axis = 1)
    return df_sub

# 2. 각 컬럼의 평균값을 구한뒤, 그 평균값으로 각 컬럼의 값을 나눈다.
def all_data_div_by_mean_value(df) :
    df_mean = df.mean()
    df_div = df.div(df_mean, axis = 1)
    return df_div

# 3. 각 컬럼의 평균값을 구한뒤, 그 평균값으로 각 컬럼의 값을 곱한다.
def all_data_mul_by_mean_value(df) :
    df_mean = df.mean()
    df_mul = df.mul(df_mean, axis = 1)
    return df_mul

#! 일부 값을 np.nan으로 변경한다.
def change_some_values_to_nan(df) :
    df.iloc[3,3] = np.nan
    df.iloc[4,4] = np.nan
    df.iloc[5,5] = np.nan
    return df

def change_some_values_to_null(df) :
    df.iloc[6,6] = None
    df.iloc[7,7] = None
    df.iloc[8,8] = None
    return df


# nan값이나 값이 비어있는 경우도 0으로 처리합니다. 
def fill_nan_null_value(df) :
    df = df.fillna(0)
    df = df.replace('', 0)
    return df


def main() : 
    
    df = pd.DataFrame(np.random.randn(100,10), columns = list(range(1,11)))
    df = change_some_values_to_nan(df)
    df = all_data_sub_by_mean_value(df)
    df = all_data_div_by_mean_value(df)
    df = all_data_mul_by_mean_value(df)
    # 언뜻보면 문제가 없는 코드이지만, 테스트코드를 보면 문제가 있음을 알 수 있습니다. 
    # 테스트코드를 통해 문제가 있는 코드를 수정해보겠습니다.
    

if __name__ == '__main__' : 
    main()
    