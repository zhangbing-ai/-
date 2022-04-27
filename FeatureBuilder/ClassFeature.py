from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
'''
有7个大类，每个大类有5个小类
print(train_inte['sub_class'].unique())
print(train_data['class'].unique())
print(test_public['class'].unique())
['B5' 'C3' 'D2' 'B1' 'C5' 'A5' 'C1' 'B4' 'A1' 'D1' 'C4' 'E2' 'C2' 'D4'
 'E3' 'D3' 'A4' 'B3' 'A3' 'E5' 'B2' 'G5' 'A2' 'F3' 'D5' 'E1' 'F4' 'F1'
 'F5' 'F2' 'G1' 'E4' 'G2' 'G3' 'G4']
['C' 'A' 'B' 'D' 'E' 'F' 'G']
['B' 'C' 'D' 'A' 'E' 'F' 'G']
'''
def feature_Kmeans(data, label):
    '''
    通过将每一个大类聚成5个小类
    :param data:
    :param label: 大类的类别
    :return:
    '''
    mms = MinMaxScaler()
    feats = [f for f in data.columns if f not in ['loan_id', 'user_id', 'isDefault']]
    data = data[feats]
    mmsModel = mms.fit_transform(data.loc[data['class'] == label])
    clf = KMeans(5, random_state=2021)
    pre = clf.fit(mmsModel)
    test = pre.labels_
    final_data = pd.Series(test, index=data.loc[data['class'] == label].index)
    if label == 1:
        final_data = final_data.map({0: 'A1', 1: 'A2', 2: 'A3', 3: 'A4', 4: 'A5'})
    elif label == 2:
        final_data = final_data.map({0: 'B1', 1: 'B2', 2: 'B3', 3: 'B4', 4: 'B5'})
    elif label == 3:
        final_data = final_data.map({0: 'C1', 1: 'C2', 2: 'C3', 3: 'C4', 4: 'C5'})
    elif label == 4:
        final_data = final_data.map({0: 'D1', 1: 'D2', 2: 'D3', 3: 'D4', 4: 'D5'})
    elif label == 5:
        final_data = final_data.map({0: 'E1', 1: 'E2', 2: 'E3', 3: 'E4', 4: 'E5'})
    elif label == 6:
        final_data = final_data.map({0: 'F1', 1: 'F2', 2: 'F3', 3: 'F4', 4: 'F5'})
    elif label == 7:
        final_data = final_data.map({0: 'G1', 1: 'G2', 2: 'G3', 3: 'G4', 4: 'G5'})
    return final_data

def data_concat(df):
    '''
    用于训练集和测试集合并
    :param df: 
    :return:
    '''
    df1 = feature_Kmeans(df, 1)
    df2 = feature_Kmeans(df, 2)
    df3 = feature_Kmeans(df, 3)
    df4 = feature_Kmeans(df, 4)
    df5 = feature_Kmeans(df, 5)
    df6 = feature_Kmeans(df, 6)
    df7 = feature_Kmeans(df, 7)
    train_dataall = pd.concat(
        [df1, df2, df3, df4, df5, df6, df7]).reset_index(
        drop=True)
    df['sub_class'] = train_dataall
    return df