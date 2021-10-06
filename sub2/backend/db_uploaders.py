import csv
import os
import django
import sys

os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings.base")	# 1. 여기서 프로젝트명.settings입력
django.setup()

# 위의 과정까지가 python manage.py shell을 키는 것과 비슷한 효과

from collections import defaultdict

codelist = defaultdict(str)
tourdetaillist = defaultdict(str)
CSV_PATH = './service.csv'	# 3. csv 파일 경로
    
    
with open(CSV_PATH, newline='') as csvfile:	# 4. newline =''
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        codelist[row['cat3']] += row['type']
        tourdetaillist[row['cat3']] += row['소분류']

# print(codelist)



from tour.models import Touristspot	# 2. App이름.models
def tourist_youngje():
    CSV_PATH = './tour.csv'	# 3. csv 파일 경로
    category_list = {
    '관광농원/허브마을': '관광지',
    '대형호수/저수지':'관광지',
    '동물원':'문화시설',
    '먹거리/패션거리':'음식',
    '서원/향교/서당':'문화시설',
    '세븐럭카지노':'문화시설',
    '숲':'관광지',
    '식물원':'관광지',
    '아쿠아리움/대형수족관':'문화시설',
    '유명관광지':'관광지',
    '유명사찰':'관광지',
    '일반관광지':'관광지',
    '일반유원지/일반놀이공원':'관광지',
    '지역사찰':'관광지',
    '지역축제':'문화시설',
    '지역호수/저수지':'관광지',
    '카지노':'문화시설',
    '테마공원/대형놀이공원':'문화시설',
    '토속/특산물/기념품매장':'문화시설',
    '파라다이스카지노':'문화시설',
    '폭포/계곡':'관광지',
    '해수욕장':'관광지',
    '휴양림/수목원':'관광지'
    }
    with open(CSV_PATH, newline='') as csvfile:	# 4. newline =''
        data_reader = csv.DictReader(csvfile)

        for row in data_reader:
            print(row)
            Touristspot.objects.create(		# 5. class명.objects.create
                title = row['poi_nm'],
                category = category_list[row['mcate_nm']],
                categorydetail = row['mcate_nm'],
                latitude = row['x'],
                longitude = row['y'],
                address = row['address'],
                code = row['code'],
                # 6
            )

def tourist_gwuanghun():
    CSV_PATH = './전처리_광훈.csv'	# 3. csv 파일 경로
    
    
    with open(CSV_PATH, newline='', encoding='utf-8-sig') as csvfile:	# 4. newline =''
        data_reader = csv.DictReader(csvfile)

        for row in data_reader:


            Touristspot.objects.create(		# 5. class명.objects.create
                title = row['title'],
                category = codelist[row['cat3']],
                categorydetail = tourdetaillist[row['cat3']],
                latitude = row['mapx'],
                longitude = row['mapy'],
                address = row['addr1'],
                code = row['code'],
                # 6
            )
    
from accounts.models import *
from tour.models import *
def review():
    CSV_PATH = './review2.csv'	# 3. csv 파일 경로
    
    
    with open(CSV_PATH, newline='') as csvfile:	# 4. newline =''
        data_reader = csv.DictReader(csvfile)

        for row in data_reader:
            if User.objects.filter(nickname=row['UserID']):
                pass
            else:
                nickname = row['UserID']
                User.objects.create(username=f'{nickname}@test.com',nickname=nickname)
            y,m,d,s= row['Timestamp'].split('.')
            Review.objects.create(
                user = User.objects.get(nickname=row['UserID']),
                Touristspot = Touristspot.objects.get(pk=row['Spot_pk']), 
                rating = row['Rating'],
                content = row['review'],
                created_at = f'{y}-{m}-{d}'
            )
            tourist_instance = Touristspot.objects.get(pk=row['Spot_pk'])
            tourist_instance.counting += 1
            tourist_instance.save()     



def images():
    CSV_PATH = './img.csv'	# 3. csv 파일 경로
    
    
    with open(CSV_PATH, newline='') as csvfile:	# 4. newline =''
        data_reader = csv.DictReader(csvfile)

        for row in data_reader:
            if row['ImgURL'] :  
                ToruistImg.objects.create(
                    Touristspot = Touristspot.objects.get(pk=row['Spot_pk']), 
                    images = row['ImgURL']
                )
# tourist_youngje()
# tourist_gwuanghun()
# review()
# images()

import requests
import json
import boto3
import uuid
from PIL import Image
from io  import BytesIO
def test():
    '''
    i : spot_id로 찾아서 img가 있는지 체크 한다 .
    없으면 api로 이미지 검색 후 하나 저장하고 s3에 올린다
    s3 올릴때 pk와 awsimages uuid 저장한다.
    59018
    '''
    for i in range(9755,59018):
        print(i)
        try : 

            if not ToruistImg.objects.filter(Touristspot = i).exists():
                if not Touristspot.objects.filter(pk=i).exists():
                    continue
                obj = Touristspot.objects.get(pk = i)
                title = obj.title
                print('---이미지 검색 시작---',title)
                url = "https://dapi.kakao.com/v2/search/image"
                headers = {
                    "Authorization" : "KakaoAK 84c4793d7481a469466d29f71665395f"
                }
                data = {
                    "query" : title,
                    "size"  : "1"
                }
                response = requests.post(url, headers=headers, data=data)
                
                # 요청에 실패했다면,
                if response.status_code != 200 or not response.json()['documents']:
                    continue
                else: # 성공했다면,
                    print('이미지 저장 시작')
                    url = response.json()['documents'][0]['image_url']
                    img_response = requests.get(url,verify=False)
                    s3_client = boto3.client(
                        's3',
                        aws_access_key_id     = 'AKIA3QQ443NJNXC2EH66',
                        aws_secret_access_key = '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'
                    )
                    # print(img_response.content)
                    if img_response.status_code == 200:
                        #print(img_response.content)

                        print("========= [이미지 저장] =========")
                        with open('test.jpg', 'wb') as fp:
                            fp.write(img_response.content)

                        image = Image.open("test.jpg")
                        buffer = BytesIO()
                        image = image.convert("RGB")
                        image.save(buffer, "JPEG")
                        buffer.seek(0)
                        url_generator = str(uuid.uuid4())
                    
                        ToruistImg.objects.create(
                            images = url,
                            Touristspot = Touristspot.objects.get(pk=i), 
                            awsimages = url_generator
                        )
                        print(url_generator)
                        s3_client.upload_fileobj(buffer,"go-test-buket",url_generator,ExtraArgs = {"ContentType": 'image/jpeg'})
        except:
            continue

test()
def delete():
    CSV_PATH = './sss.csv'	# 3. csv 파일 경로
    
    
    with open(CSV_PATH, newline='') as csvfile:	# 4. newline =''
        data_reader = csv.DictReader(csvfile)

        for row in data_reader:
            print(row['id'])
            obj =Touristspot.objects.get(pk=row['id'])
            # if ToruistImg.objects.filter(Touristspot = row['id']).exists():

            # list2 = Review.objects.filter(Touristspot = row['id'])
            # list3 = WishList.objects.filter(Touristspot = row['id'])
            # list4 = RouteTouristspot.objects.filter(touristspot = row['id'])
            # list.delete()
            # list2.delete()
            # list3.delete()
            # list4.delete()
            # print(obj)
            obj.delete()

# delete()