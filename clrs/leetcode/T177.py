# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/23 11:46 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""

import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = employee[['salary']].drop_duplicates().sort_values("salary", ascending=False)
    # print(unique_salaries)
    if len(unique_salaries) < N:
        return pd.DataFrame({'getNthHighestSalary(2)': [None]})
    return unique_salaries.head(N).tail(1)


def nth_highest_salary2(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee[["salary"]].drop_duplicates().s
    if len(df) < N:
        return pd.DataFrame({'getNthHighestSalary(2)': [None]})
    return df.sort_values("salary", ascending=False).head(N).tail(1)


if __name__ == "__main__":
    # 创建示例的 Employee 表
    employee_data = {'id': [1, 2, 3],
                     'salary': [100, 200, 300]}
    employee_df = pd.DataFrame(employee_data)

    # 调用函数，输出结果
    result_df = nth_highest_salary(employee_df, 2)
    print(result_df)
