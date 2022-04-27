from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def encoder_feature(df):
    cat_cols = ['employer_type', 'industry']
    for col in cat_cols:
        lbl = LabelEncoder().fit(df[col])
        df[col] = lbl.transform(df[col])  # 进行类别编码
    return df

