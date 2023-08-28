import requests as req
import pandas as pd
import re
import datetime
import time
from bs4 import BeautifulSoup
from marcap import marcap_data
from tqdm import tqdm

class dataColledctionCLs:

    def discussionData(self, codes):
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

        pages = range(1, 2)
        codes = codes[0:20]
        df = pd.DataFrame(columns=range(4))
        df.columns = ['code', 'date', 'title', 'contents']

        for code in tqdm(codes):
            for page in pages:
                urls = f'https://finance.naver.com/item/board.naver?code={str(code)}&page={str(page)}'
                response = req.get(urls, headers=headers)
                soup = BeautifulSoup(response.text, 'html.parser')

                aa = soup.select("tr[onmouseover='mouseOver(this)'] td:nth-child(1) span")
                bb = soup.find_all(href=re.compile("/item/board_read.naver")) # re.compile() 정규 파일 오브젝트 생성

                for a, b in zip(aa, bb):
                    dt = datetime.datetime.strptime(a.contents[0].split(' ')[0].replace('.', '-'), '%Y-%m-%d')
                    link = b['href']
                    title = b['title']

                    response2 = req.get(https://finance.naver.com' + link, headers=headers)
                    soup2 = BeautifulSoup(response2.text, 'html.parser')

                    df.loc[len(df)] = [code, dt, title, soup2.find(id='body').find_all(text=True)]

                time.sleep(1)

        df.to_csv('output_pd.csv')

    def stockData(self,stday):
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        # 특정기간 전종목 가져오기(시간 형식: %Y-%m-%d)
        df = marcap_data(stday, today) # 2015.06.15부터 상한가 폭 변경

    def codeData(self):
        today = datetime.datetime.today()
        dayago = today - datetime.timedelta(days=7)
        df = marcap_data(dayago.strftime('%Y-%m-%d'), today.strftime('%Y-%m-%d'))
        df = df.loc[df['Market'] != 'KONEX'] # KONEX 제거

        arr_code = df.Code.unique() # class 'numpy.ndarray'
        print(arr_code)
        return arr_code
