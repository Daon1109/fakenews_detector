import pandas as pd
import modules

# 데이터 전처리
df_t = pd.read_csv('C:/Programming_2023/dataset/True.csv')
modules.preprocess(df_t, 'True')
df_f = pd.read_csv('C:/Programming_2023/dataset/Fake.csv')
modules.preprocess(df_t, 'False')

# TF-IDF 계산
modules.TF_IDF()
