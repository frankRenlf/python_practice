# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/23 12:20 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""

import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    result = employee.merge(employee, left_on='managerId', right_on='id', suffixes=('', '_manager'))
    result_filtered = result[result['salary'] > result['salary_manager']]
    result_filtered['Employee'] = result_filtered['name']

    return result_filtered[['Employee']]
# if __name__ == "__main__":
