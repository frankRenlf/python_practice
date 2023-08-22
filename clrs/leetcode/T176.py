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
    data = employee.loc[1:, 'salary']
    val = None
    if len(data) > 1:
        val = sorted(data, reverse=True)
    return pd.DataFrame({'SecondHighestSalary': [val[1]]})


if __name__ == "__main__":
    # 创建示例的 Employee 表
    employee_data = {'id': [1, 2, 3],
                     'salary': [100, 200, 300]}
    employee_df = pd.DataFrame(employee_data)

    # 调用函数，输出结果
    result_df = second_highest_salary(employee_df)
    print(result_df)
