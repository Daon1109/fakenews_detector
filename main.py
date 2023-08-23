import pandas as pd
import re

df_fake = pd.read_csv('C:/Programming_2023/dataset/test_fake.csv', encoding='utf-8')
subject_drop_a = df_fake['date']
subject_drop_b = df_fake['title']
#normalstate = ['News','politics','Government News','left-news','US_News','Middle-east']


# 데이터 전처리: 칸 벗어남
for i in range(len(subject_drop_a)):
    
    print(i)
    if subject_drop_a[i][0] == ' ':
        df_fake.drop(i)
        print('dropped')
    elif int(subject_drop_a[i][0]) == 0 or int(subject_drop_a[i][0]) == 1 or int(subject_drop_a[i][0]) == 2 or int(subject_drop_a[i][0]) == 3:
        pass
    else:
        df_fake.drop(i)
        print('dropped')

        
# 데이터 전처리: 한글 깨짐 현상
for i in range(len(subject_drop_b)):
    
    print(i)
    if re.findall(r'[가-힣]', subject_drop_b[i]):
        df_fake.drop(i)
        print('dropped')    
    else:
        pass    
        

print(df_fake)