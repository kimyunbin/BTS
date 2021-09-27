from rest_framework.response import Response

import requests
import datetime
import pandas as pd
import json
# 영화 데이터 데이터베이스에 넣기 

def movie_data2() :
    link = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?ServiceKey=ZEnJ%2F%2BhPv2A5965%2BZ0OVAqXpuZGiaQQqzoWpuu5UomOsu0Y3G%2BdKybUyrPlImH8h1tBNanqIkfNeNQDByzTXHw%3D%3D&MobileApp=AppTest&MobileOS=ETC&_type=json&numOfRows=5000000"
    
    res = requests.get(link)
    
    data_list = res.json()['response']['body']['items']['item']

    df = pd.json_normalize(data_list)
    df.to_csv("samplecsv.csv",encoding='utf-8-sig')
