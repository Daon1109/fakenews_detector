
import pandas
import warnings
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import re



# 데이터 전처리
def preprocess(df, string):
    
    subject_drop_a = df['date']
    subject_drop_b = df['title']
    for i in range(len(subject_drop_a)):
        print(i)
        droped = 0
        
        # 데이터 전처리: NULL
        if not subject_drop_a[i]:
            df = df.drop(index=i, axis=0)
            droped = 1
            print('dropped')
        # 데이터 전처리: 칸 벗어남
        elif subject_drop_a[i][0] == ' ':
            df = df.drop(index=i, axis=0)
            droped = 1
            print('dropped')
            
        elif int(subject_drop_a[i][0]) in [0,1,2,3,4,5,6,7,8,9]:
            pass
        else:
            df = df.drop(index=i, axis=0)
            droped = 1
            print('dropped')
        # 중복 방지
        if droped == 1:
            pass
        # 데이터 전처리: 한글 깨짐 현상
        else:
            if re.findall(r'[가-힣]', subject_drop_b[i]):
                df = df.drop(index=i, axis=0)
                print('dropped')    
            else:
                pass
    # result
    print(df)

    # 전처리된 데이터 저장
    df.to_csv("C:/Programming_2023/dataset/{}.csv".format(string), index = True)
    



# TF-IDF 계산(키워드추출): 1학년 작업
def TF_IDF():
    
    # 데이터 읽기
    True_data = pandas.read_csv("C:/Programming_2023/dataset/True.csv")
    Fake_data = pandas.read_csv("C:/Programming_2023/dataset/Fake.csv")

    # 뉴스 레이블링 및 병합 / 1:True News / 0:Fake News
    True_data['label'] = 1 
    Fake_data['label'] = 0
    data = pandas.concat([True_data,Fake_data],axis=0)

    # Text 컬럼과 Label 이외에 다른 부가 정보 버리기
    data.drop(['title','subject','date'],axis=1, inplace=True)

    # 데이터 10개만 임시로 출력해서 결과물 확인하기
    data.head(10)

    # 라이브러리 버전 관련 이슈를 알려주는 불필요한 메세지를 안 보이게 하기
    warnings.filterwarnings(action='ignore')
    # NLTK 로드하기
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    # NLTK 패키지 불러오기
    from nltk import pos_tag, word_tokenize

    # 명사, 동사, 형용사, 부사 어휘 추출 전처리 함수
    def filter_words_by_pos(sentence, pos_tags):
        words = word_tokenize(sentence)
        tagged_words = pos_tag(words)
        filtered_words = [word for word, pos in tagged_words if pos in pos_tags and word!="“" and word!="”"]
        return filtered_words

    # 전처리 함수 사용 예시 및 결과물
    print("전처리 수행 전 뉴스 기사 원문 내용")
    print("-"*100)
    print(data.iloc[0,0])

    print("-"*100)
    print("전처리 수행 후 뉴스 기사 원문 내 어휘")
    print("-"*100)
    filtered_words = filter_words_by_pos(data.iloc[0,0], ['NN', 'VB', 'JJ', 'RB'])
    print(filtered_words)
    # 모든 데이터에 대해 전처리 수행 (시간 소요 필요)
    data['text'] = data.apply(lambda x: " ".join(filter_words_by_pos(x['text'],['NN', 'VB', 'JJ', 'RB'])), axis=1)

    # 추출된 명사(Noun), 동사(Verb), 형용사(Adjective), 부사(Adverb)들을 TF-IDF로 정형화 & 빈도수 기반 상위 100개의 단어 사용
    vectorizer_final = TfidfVectorizer(max_features=100)
    tf_idf = vectorizer_final.fit_transform(data['text'].values)
    tf_idf = pandas.DataFrame(tf_idf.toarray(), columns=vectorizer_final.get_feature_names_out(), index=data.index)

    # TF-IDF 데이터프레임에 Label 컬럼 추가 --> 결론적으로, TF-IDF 데이터 프레임 내에 입력 변수 (X(=TF-IDF), 출력 변수 (뉴스 기사 진위 여부)가 모두 포함됨
    tf_idf['label'] = data['label']
    tf_idf = tf_idf.reset_index(drop=True)
    tf_idf.to_csv("C:/Programming_2023/dataset/tf_idf_result.csv", index=True)
