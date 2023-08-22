# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/23 00:57 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""
import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # 去除重复的薪水值，并按薪水值降序排列
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    # 如果只有一个薪水值，或者没有薪水值，结果为 null，否则取第二个薪水值
    if len(unique_salaries) <= 1:
        result = None
    else:
        result = unique_salaries.iloc[1]
    # 创建包含结果的 DataFrame
    return pd.DataFrame({'SecondHighestSalary': [result]})


if __name__ == "__main__":
    # 创建示例的 Employee 表
    employee_data = {'id': [1, 2, 3],
                     'salary': [100, 200, 300]}
    employee_df = pd.DataFrame(employee_data)

    # 调用函数，输出结果
    result_df = second_highest_salary(employee_df)
    print(result_df)
