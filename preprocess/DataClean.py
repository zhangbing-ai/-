import pandas as pd
import numpy as np
import re

'''
train_public: 39列
Index(['loan_id', 'user_id', 'total_loan', 'year_of_loan', 'interest',
       'monthly_payment', 'class', 'employer_type', 'industry', 'work_year',
       'house_exist', 'censor_status', 'issue_date', 'use', 'post_code',
       'region', 'debt_loan_ratio', 'del_in_18month', 'scoring_low',
       'scoring_high', 'known_outstanding_loan', 'known_dero',
       'pub_dero_bankrup', 'recircle_b', 'recircle_u', 'initial_list_status',
       'app_type', 'earlies_credit_mon', 'title', 'policy_code', 'f0', 'f1',
       'f2', 'f3', 'f4', 'early_return', 'early_return_amount',
       'early_return_amount_3mon', 'isDefault'],
      dtype='object')
test_public: 38列
Index(['loan_id', 'user_id', 'total_loan', 'year_of_loan', 'interest',
       'monthly_payment', 'class', 'employer_type', 'industry', 'work_year',
       'house_exist', 'censor_status', 'issue_date', 'use', 'post_code',
       'region', 'debt_loan_ratio', 'del_in_18month', 'scoring_low',
       'scoring_high', 'known_outstanding_loan', 'known_dero',
       'pub_dero_bankrup', 'recircle_b', 'recircle_u', 'initial_list_status',
       'app_type', 'earlies_credit_mon', 'title', 'policy_code', 'f0', 'f1',
       'f2', 'f3', 'f4', 'early_return', 'early_return_amount',
       'early_return_amount_3mon'],
      dtype='object')
train_internet: 42列
Index(['loan_id', 'user_id', 'total_loan', 'year_of_loan', 'interest',
       'monthly_payment', 'class', 'sub_class', 'work_type', 'employer_type',
       'industry', 'work_year', 'house_exist', 'house_loan_status',
       'censor_status', 'marriage', 'offsprings', 'issue_date', 'use',
       'post_code', 'region', 'debt_loan_ratio', 'del_in_18month',
       'scoring_low', 'scoring_high', 'pub_dero_bankrup', 'early_return',
       'early_return_amount', 'early_return_amount_3mon', 'recircle_b',
       'recircle_u', 'initial_list_status', 'earlies_credit_mon', 'title',
       'policy_code', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'is_default'],
      dtype='object')
'''
# 读取数据
train_data = pd.read_csv('../data/train_public.csv')
test_data = pd.read_csv('../data/test_public.csv')
train_internet = pd.read_csv('../data/train_internet.csv')

print(train_data['post_code'].mode())


def missing_data_processing(table, if_title):
    '''
    填充缺失值
    :if_title: 0 or 1, 表示title这个字段是否存在
    '''
    loss_numerical_feas = ['recircle_u', 'pub_dero_bankrup', 'debt_loan_ratio']
    f_feas = ['f0', 'f1', 'f2', 'f3', 'f4']
    table[loss_numerical_feas] = table[loss_numerical_feas].fillna(table[loss_numerical_feas].median())
    table[f_feas] = table[f_feas].fillna(table[f_feas].median())
    table.post_code = table.post_code.fillna(table.post_code.mode()[1])
    table.loc[table.debt_loan_ratio < 0, 'debt_loan_ration'] = 0
    if if_title: # 如果title这个字段存在
        table.title = table.title.fillna(table.title.mode()[1])


def workYearDic(x):
    '''
    将工作年限转换为数字
    :param x:
    :return:
    '''
    if str(x) == 'nan':
        return 0
    x = x.replace('<1', '0')
    # (\d+)该正则表达式用于选取出字符串中的数字
    return int(re.search('(\d+)', x).group())

def strToNum(df):
    '''
    工作年限字符串数据转换为数值
    class类别型数据编码

    :param df:
    :return:
    '''
    class_dict = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
    }
    df['work_year'] = df['work_year'].map(workYearDic)
    df['class'] = df['class'].map(class_dict)
    return df

def findDig(val):
    '''
    将日期转换为相同格式
    :param val:
    :return:
    '''
    fd = re.search('(\d+-)', val)
    if fd is None:
        return '1-' + val
    return val + '-01'

def timeStandard(df, if_internt):
    '''
    日期标准化
    对于异常的日期值减去100年
    :param df:
    :if_internet: 判断是否为internet数据
    :return:
    '''
    timeMax = pd.to_datetime('1-Dec-21')
    df.issue_date = pd.to_datetime(df.issue_date)
    if if_internt:
        df.earlies_credit_mon = pd.to_datetime(df.earlies_credit_mon)
    else:
        df.earlies_credit_mon = pd.to_datetime(df.earlies_credit_mon.map(findDig))
        df.loc[df.earlies_credit_mon > timeMax, 'earlies_credit_mon'] = df.loc[
                                                                            df.earlies_credit_mon > timeMax, 'earlies_credit_mon'] + pd.offsets.DateOffset(years = -100)

    return df

def drop_columns(df):
    '''
    删除无关列
    :param df:
    :return:
    '''
    col_to_drop = ['issue_date', 'earlies_credit_mon']
    df = df.drop(col_to_drop, axis=1)
    return df






