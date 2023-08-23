import pandas as pd
import re

df_fake = pd.read_csv('C:/Coding/AI&ML/Projects/fakenews_detector/data/test_fake.csv', encoding='utf-8')
#normalstate = ['News','politics','Government News','left-news','US_News','Middle-east']


# 데이터 전처리
subject_drop_a = df_fake['date']
subject_drop_b = df_fake['title']
for i in range(len(subject_drop_a)):
    
    print(i)
    droped = 0
    
    # 데이터 전처리: 칸 벗어남
    if subject_drop_a[i][0] == ' ':
        df_fake = df_fake.drop(index=i, axis=0)
        droped = 1
        print('dropped')
    elif int(subject_drop_a[i][0]) in [0,1,2,3,4,5,6,7,8,9]:
        pass
    else:
        df_fake = df_fake.drop(index=i, axis=0)
        droped = 1
        print('dropped')

    # 중복 방지
    if droped == 1:
        pass
    
    # 데이터 전처리: 한글 깨짐 현상
    else:
        if re.findall(r'[가-힣]', subject_drop_b[i]):
            df_fake = df_fake.drop(index=i, axis=0)
            print('dropped')    
        else:
            pass


# 전처리된 데이터 저장
df_fake.to_csv("C:/Coding/AI&ML/Projects/fakenews_detector/data/data_preprocessed.csv", index = True)



# result
print(df_fake)
