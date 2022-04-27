
def time_feature(df):
    df['issue_date_month'] = df['issue_date'].dt.month
    df['issue_date_year'] = df['issue_date'].dt.year
    df['issue_date_dayofweek'] = df['issue_date'].dt.dayofweek
    df['earliesCreditMon'] = df['earlies_credit_mon'].dt.month
    df['earliesCreditYear'] = df['earlies_credit_mon'].dt.year
    return df