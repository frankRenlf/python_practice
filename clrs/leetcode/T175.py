# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/23 00:38 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""

import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    res = pd.merge(person, address, how='left', on='personId')
    return res.loc[:, ['firstName', 'lastName', 'city', 'state']]


if __name__ == "__main__":
    # 创建示例的 Person 表和 Address 表
    person_data = {'personId': [1, 2],
                   'lastName': ['Wang', 'Alice'],
                   'firstName': ['Allen', 'Bob']}
    address_data = {'addressId': [1, 2],
                    'personId': [2, 3],
                    'city': ['New York City', 'Leetcode'],
                    'state': ['New York', 'California']}

    person_df = pd.DataFrame(person_data)
    address_df = pd.DataFrame(address_data)

    # 调用函数，输出结果
    result_df = combine_two_tables(person_df, address_df)
    print(result_df)
