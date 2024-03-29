import pandas as pd
import numpy as np
from konlpy.tag import Twitter
from tqdm import tqdm

class dataPreprocessingCls:
    def __init__(self):
        self.coin_df = pd.read_csv('../stock-eda-project/stockdata/coin.csv')
        self.exchange_df = pd.read_csv('../stock-eda-project/stockdata/exchange.csv')
        self.indexDJI_df = pd.read_csv('../stock-eda-project/stockdata/indexDJI.csv')
        self.indexIXIC_df = pd.read_csv('../stock-eda-project/stockdata/indexIXIC.csv')
        self.indexKQ11_df = pd.read_csv('../stock-eda-project/stockdata/indexKQ11.csv')
        self.indexKS11_df = pd.read_csv('../stock-eda-project/stockdata/indexKS11.csv')
        self.indexUS500_df = pd.read_csv('../stock-eda-project/stockdata/indexUS500.csv')
        self.stock_df = pd.read_csv('../stock-eda-project/stockdata/stock.csv')
        self.daum_df = pd.read_csv('../stock-eda-project/daum/output.csv', dtype=object)


    def stockPreprocessing(self): # 주식 데이터 전처리
        pass

    def discussionPreprocessing(self): # 주식 + 종토방 데이터 전처리
        df = self.daum_df.copy()
        df = df[['Title','Contents']]
        twt = Twitter()

        # 형태소 분석
        sy = []
        for i in df['Contents']:
            tagging = twt.pos(i)
            print(tagging)
            for i, j in tagging:
                # '동사', '명사'만 추출
                if j == 'Noun' or j == 'Verb':
                    sy.append(i)



        #df = pd.merge(self.stock_df, self.discuss_df, how='inner', on=['Code', 'Date'])
        #print(df)

st = dataPreprocessingCls()
st.discussionPreprocessing()
