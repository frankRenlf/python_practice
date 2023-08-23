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
    result_filtered.loc[:, ('Employee')] = result_filtered['name']

    return result_filtered[['Employee']]


def find_employees2(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(employee[['id', 'salary']], how='left', left_on='managerId', right_on='id')
    return df.loc[df['salary_x'] > df['salary_y'], ['name']].rename(columns={'name': 'Employee'})


if __name__ == "__main__":
    # Test
    data = {'id': [1, 2, 3, 4],
            'name': ['Joe', 'Henry', 'Sam', 'Max'],
            'salary': [70000, 80000, 60000, 90000],
            'managerId': [3, 4, None, None]}
    employee_df = pd.DataFrame(data)
    output = find_employees2(employee_df)
    print(output)
