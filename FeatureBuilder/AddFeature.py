
def addFeature(df):
    # 对于每一种行业，计算f系列特征的均值
    f_feas = ['f0', 'f1', 'f2', 'f3', 'f4']
    for f in f_feas:
        df[f'industry_to_mean_{f}'] = df.groupby('industry')[f].transform('mean')