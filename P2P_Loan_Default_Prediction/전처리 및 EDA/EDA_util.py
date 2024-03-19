'''데이터 셋 EDA를 할 때 유용하게 쓰이는 함수 모음집입니다.
'''
def make_na_table(features, df):
    '''
    features의 결측치의 개수와, 전체 데이터 셋에서 차지하는 비율을 PrettyTable로 보여줍니다.
    
    Parameters:
    -----------
    features : list
        결측치를 확인하고 싶은 컬럼을 리스트 형태로 전달합니다.
    df : pandas DataFrame, optional
        결측치를 확인할 데이터프레임입니다. 기본값은 전역 변수 df입니다.
        
    Returns:
    --------
    None
    
    Examples:
    ---------
    >>> make_na_table(['Age', 'Sex', 'Embarked'])
    +----------+------------+----------+
    | 변수명 | 결측치 개수 | 전체 비율 |
    +----------+------------+----------+
    |   Age    |     177        |   19.87%  |
    |   Sex    |      0          |    0.00%  |
    |Embarked|      2          |    0.22%  |
    +----------+------------+----------+
    '''
    na_table = PrettyTable()
    na_table.field_names = ["변수명", "결측치 개수", "전체 비율"]
    for col in features:
        na_cnt = df[col].isna().sum()
        total_rows = df.shape[0]
        ratio = (na_cnt / total_rows) * 100
        na_table.add_row([col, na_cnt, f'{ratio:.2f}%'])
    print(na_table)
    


def get_uv_nlist(features, n, df):
    '''
    features의 유니크 값의 개수가 n개인 컬럼을 찾아 출력합니다.
    
    Parameters:
    -----------
    features : list
        유니크 값을 확인하고 싶은 컬럼을 리스트 형태로 전달합니다.
    n : int
        유니크 값의 개수가 n개이하인 컬럼의 유니크 값을 찾기 위한 기준 값입니다.
    df : pandas DataFrame
        유니크 값을 확인할 데이터프레임입니다.
        
    Returns:
    --------
    list
        유니크 값의 개수가 n개인 컬럼의 리스트를 반환합니다.
    '''
    selected_cols = []
    for col in features:
        unique_count = df[col].nunique()
        
        if unique_count <= n:
            selected_cols.append(col)
            print(f'{col}의 유니크 값 개수: {unique_count}')
            print(df[col].unique(), '\n')
            print('-' * 70)
        else:
            print(f'{col}의 유니크 값 개수: {unique_count}')
            print('!!!Too Many!!!\n', df[col].unique()[1:5])
            print('-' * 70)
    return selected_cols




class OutlierHandler:
    """
    데이터프레임에서 이상치를 처리하기 위한 클래스입니다.
    """
    def __init__(self, df):
        self.df = df
    
    def get_outlier_thresholds(self, variable):
        """
        주어진 변수의 이상치 경계를 반환합니다.

        Returns:
        --------
        tuple
            이상치의 하한 경계와 상한 경계를 포함한 튜플을 반환합니다.
        """
        Q1 = self.df[variable].quantile(0.25)
        Q3 = self.df[variable].quantile(0.75)
        IQR_range = Q3 - Q1
        up_fence = Q3 + 1.5 * IQR_range
        low_fence = Q1 - 1.5 * IQR_range
        return low_fence, up_fence
    
    def count_outliers(self, variable):
        """
        주어진 변수의 이상치 개수를 반환합니다.
        
        Returns:
        --------
        int
            이상치의 개수를 반환합니다.
        """
        Q1 = self.df[variable].quantile(0.25)
        Q3 = self.df[variable].quantile(0.75)
        IQR_range = Q3 - Q1
        up_fence = Q3 + 1.5 * IQR_range
        low_fence = Q1 - 1.5 * IQR_range
        outliers_count = self.df[(self.df[variable] < low_fence) | (self.df[variable] > up_fence)].shape[0]
        return outliers_count
    
    def replace_with_thresholds(self, variable, low_fence, up_fence):
        """
        주어진 변수의 이상치를 이상치 경계로 대체합니다.

        Parameters:
        -----------
        variable : str
            이상치를 대체하고자 하는 변수의 이름입니다.
        low_fence : float
            이상치를 대체할 값으로 설정할 이상치 하한 경계값입니다.
        up_fence : float
            이상치를 대체할 값으로 설정할 이상치 상한 경계값입니다.

        Returns:
        --------
        pandas DataFrame
            이상치가 대체된 데이터프레임을 반환합니다.
        """
        self.df.loc[(self.df[variable] < low_fence), variable] = low_fence
        self.df.loc[(self.df[variable] > up_fence), variable] = up_fence
        return self.df










