from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import City
from django.contrib.auth import get_user_model
from .models import User
import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from django.db.models import Q
citys = [11010, 11020, 11030, 11040, 11050, 11060, 11080, 11090, 11100, 11110, 11120, 11130, 11140, 11150, 11160, 11170, 11180, 11190, 11210, 11220, 11230, 11240, 11250, 21010, 21020, 21030, 21040, 21050, 21060, 21070, 21080, 21090, 21100, 21110, 21120, 21130, 21140, 21310, 22010, 22020, 22040, 22050, 22060, 22070, 22310, 23010, 23020, 23030, 23040, 23050, 23060, 23070, 23080, 23310, 23320, 24010, 24020, 24030, 24040, 24050, 25010, 25020, 25030, 25040, 25050, 26010, 26020, 26030, 26040, 26310, 29010, 31010, 31020, 31030, 31040, 31050, 31060, 31070, 31080, 31090, 31100, 31110, 31120, 31130, 31140, 31150, 31160, 31170, 31180, 31190, 31200, 31210, 31220, 31230, 31240, 31250, 31260, 31270, 31280, 31350, 31370, 31380, 32010, 32020, 32030, 32040, 32050, 32060, 32070, 32310, 32320, 32330, 32340, 32350, 32360, 32370, 32390, 32400, 32410, 33020, 33030, 33040, 33320, 33330, 33340, 33350, 33360, 33370, 33380, 33390, 34010, 34020, 34030, 34040, 34050, 34060, 34070, 34080, 34310, 34330, 34340, 34350, 34360, 34370, 34380, 35010, 35020, 35030, 35040, 35050, 35060, 35310, 35320, 35330, 35340, 35350, 35360, 35370, 35380, 36010, 36020, 36030, 36040, 36060, 36310, 36320, 36330, 36350, 36360, 36370, 36380, 36390, 36400, 36410, 36420, 36430, 36440, 36450, 36460, 36470, 36480, 37010, 37020, 37030, 37040, 37050, 37060, 37070, 37080, 37090, 37100, 37310, 37320, 37330, 37340, 37350, 37360, 37370, 37380, 37390, 37400, 37410, 37420, 37430, 38030, 38050, 38060, 38070, 38080, 38090, 38100, 38110, 38310, 38320, 38330, 38340, 38350, 38360, 38370, 38380, 38390, 38400, 39010, 39020]
ages = [19,25,27,34,41,54,68,73]
state_city = {'11010':'서울특별시 종로구', '11020':'서울특별시 중구', '11030':'서울특별시 용산구','11040':'서울특별시 성동구','11050':'서울특별시 광진구','11060':'서울특별시 동대문구','11070':'서울특별시 중랑구','11080':'서울특별시 성북구','11090':'서울특별시 강북구','11100':'서울특별시 도봉구','11110':'서울특별시 노원구','11120':'서울특별시 은평구','11130':'서울특별시 서대문구','11140':'서울특별시 마포구','11150':'서울특별시 양천구','11160':'서울특별시 강서구','11170':'서울특별시 구로구','11180':'서울특별시 금천구','11190':'서울특별시 영등포구','11200':'서울특별시 동작구','11210':'서울특별시 관악구','11220':'서울특별시 서초구','11230':'서울특별시 강남구','11240':'서울특별시 송파구','11250':'서울특별시 강동구','21010':'부산광역시 중구','21020':'부산광역시 서구','21030':'부산광역시 동구','21040':'부산광역시 영도구','21050':'부산광역시 부산진구','21060':'부산광역시 동래구','21070':'부산광역시 남구','21080':'부산광역시 북구','21090':'부산광역시 해운대구','21100':'부산광역시 사하구','21110':'부산광역시 금정구','21120':'부산광역시 강서구','21130':'부산광역시 연제구','21140':'부산광역시 수영구','21150':'부산광역시 사상구','21310':'부산광역시 기장군','22010':'대구광역시 중구','22020':'대구광역시 동구','22030':'대구광역시 서구','22040':'대구광역시 남구','22050':'대구광역시 북구','22060':'대구광역시 수성구','22070':'대구광역시 달서구', '22310':'대구광역시 달성군','23010':'인천광역시 중구','23020':'인천광역시 동구','23030':'인천광역시 남구','23040':'인천광역시 연수구','23050':'인천광역시 남동구','23060':'인천광역시 부평구','23070':'인천광역시 계양구','23080':'인천광역시 서구','23090':'인천광역시 미추홀구','23310':'인천광역시 강화군','23320':'인천광역시 옹진군','24010':'광주광역시 동구','24020':'광주광역시 서구','24030':'광주광역시 남구','24040':'광주광역시 북구','24050':'광주광역시 광산구','25010':'대전광역시 동구','25020':'대전광역시 중구','25030':'대전광역시 서구','25040':'대전광역시 유성구','25050':'대전광역시 대덕구','26010':'울산광역시 중구','26020':'울산광역시 남구', '26030':'울산광역시 동구','26040':'울산광역시 북구','26310':'울산광역시 울주군','29010':'세종특별자치시 세종특별자치시','31010':'경기도 수원시','31020':'경기도 성남시','31030':'경기도 의정부시','31040':'경기도 안양시','31050':'경기도 부천시','31060':'경기도 광명시','31070':'경기도 평택시','31080':'경기도 동두천시','31090':'경기도 안산시','31100':'경기도 고양시','31110':'경기도 과천시','31120':'경기도 구리시','31130':'경기도 남양주시','31140':'경기도 오산시','31150':'경기도 시흥시','31160':'경기도 군포시','31170':'경기도 의왕시','31180':'경기도 하남시','31190':'경기도 용인시','31200':'경기도 파주시','31210':'경기도 이천시','31220':'경기도 안성시','31230':'경기도 김포시','31240':'경기도 화성시','31250':'경기도 광주시','31260':'경기도 양주시','31270':'경기도 포천시','31280':'경기도 여주시','31350':'경기도 연천군','31370':'경기도 가평군','31380':'경기도 양평군','32010':'강원도 춘천시','32020':'강원도 원주시','32030':'강원도 강릉시','32040':'강원도 동해시','32050':'강원도 태백시','32060':'강원도 속초시','32070':'강원도 삼척시','32310':'강원도 홍천군', '32320':'강원도 횡성군','32330':'강원도 영월군','32340':'강원도 평창군','32350':'강원도 정선군','32360':'강원도 철원군','32370':'강원도 화천군','32380':'강원도 양구군','32390':'강원도 인제군','32400':'강원도 고성군','32410':'강원도 양양군','33020':'충청북도 충주시','33030':'충청북도 제천시','33040':'충청북도 청주시','33320':'충청북도 보은군','33330':'충청북도 옥천군','33340':'충청북도 영동군','33350':'충청북도 진천군','33360':'충청북도 괴산군','33370':'충청북도 음성군','33380':'충청북도 단양군','33390':'충청북도 증평군','34010':'충청남도 천안시','34020':'충청남도 공주시','34030':'충청남도 보령시','34040':'충청남도 아산시','34050':'충청남도 서산시','34060':'충청남도 논산시','34070':'충청남도 계룡시','34080':'충청남도 당진시','34310':'충청남도 금산군','34330':'충청남도 부여군','34340':'충청남도 서천군','34350':'충청남도 청양군','34360':'충청남도 홍성군','34370':'충청남도 예산군','34380':'충청남도 태안군','35010':'전라북도 전주시','35020':'전라북도 군산시','35030':'전라북도 익산시','35040':'전라북도 정읍시','35050':'전라북도 남원시','35060':'전라북도 김제시','35310':'전라북도 완주군','35320':'전라북도 진안군','35330':'전라북도 무주군','35340':'전라북도 장수군','35350':'전라북도 임실군', '35360':'전라북도 순창군','35370':'전라북도 고창군','35380':'전라북도 부안군','36010':'전라남도 목포시','36020':'전라남도 여수시','36030':'전라남도 순천시','36040':'전라남도 나주시','36060':'전라남도 광양시','36310':'전라남도 담양군','36320':'전라남도 곡성군','36330':'전라남도 구례군','36350':'전라남도 고흥군','36360':'전라남도 보성군','36370':'전라남도 화순군','36380':'전라남도 장흥군','36390':'전라남도 강진군','36400':'전라남도 해남군','36410':'전라남도 영암군','36420':'전라남도 무안군','36430':'전라남도 함평군','36440':'전라남도 영광군','36450':'전라남도 장성군','36460':'전라남도 완도군','36470':'전라남도 진도군','36480':'전라남도 신안군','37010':'경상북도 포항시','37020':'경상북도 경주시','37030':'경상북도 김천시','37040':'경상북도 안동시','37050':'경상북도 구미시','37060':'경상북도 영주시','37070':'경상북도 영천시','37080':'경상북도 상주시','37090':'경상북도 문경시','37100':'경상북도 경산시','37310':'경상북도 군위군','37320':'경상북도 의성군','37330':'경상북도 청송군','37340':'경상북도 영양군','37350':'경상북도 영덕군','37360':'경상북도 청도군','37370':'경상북도 고령군','37380':'경상북도 성주군', '37390':'경상북도 칠곡군','37400':'경상북도 예천군','37410':'경상북도 봉화군','37420':'경상북도 울진군','37430':'경상북도 울릉군','38030':'경상남도 진주시','38050':'경상남도 통영시','38060':'경상남도 사천시','38070':'경상남도 김해시','38080':'경상남도 밀양시','38090':'경상남도 거제시','38100':'경상남도 양산시','38110':'경상남도 창원시','38310':'경상남도 의령군','38320':'경상남도 함안군','38330':'경상남도 창녕군','38340':'경상남도 고성군','38350':'경상남도 남해군','38360':'경상남도 하동군','38370':'경상남도 산청군','38380':'경상남도 함양군','38390':'경상남도 거창군','38400':'경상남도 합천군','39010':'제주특별자치도 제주시','39020':'제주특별자치도 서귀포시',}


def userSatis(request,user):
    budget, travelers, companion, transportation, selection, age, activity = int(request.data.get('budget')), int(request.data.get('travelers')), request.data.get('companion'), request.data.get('transportation'), request.data.get('selection'), request.data.get('age'), request.data.get('activity')
    forest = joblib.load(os.path.join(os.path.dirname(os.path.dirname(__file__)),'accounts/forest.pkl'))
    sample = [budget, budget//travelers, travelers]
    sample += list(map(int, list(activity)))
    if companion=='true':
        sample += [1,0]
    elif companion == 'false':
        sample += [0,1]
    else:
        sample += [0,0]
    sample += list(map(int, list(transportation)))
    sample += list(map(int, list(selection)))
    if int(age) < 20:
        sample += [1]
    else:
        sample += [0]
    for i in ages:
        if i == int(age):
            sample += [1]
        else:
            sample += [0]
    city_list = [0]*224
    for i in range(224):
        city_list[i] = 1
        temp = forest.predict_proba(pd.DataFrame(sample+city_list).T)[0][1]
        city_list[i] = 0
        c,s = state_city[str(citys[i])].split()
        cityObject = City(user=user, city=c, state=s, satis=temp, code=citys[i])
        cityObject.save()
        

@api_view(['POST'])
def signup(request):
	#1. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    print(request.data.get('budget'))
	#2. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
        userSatis(request, user)
        # print(user.password)
    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
    return Response( {"status": "success"},status=status.HTTP_201_CREATED)

@api_view(['POST'])
def checkusername(request):
    '''
    유저 이메일 및 닉네임 중복체크 
    '''
    username = request.data.get('username')
    nickname = request.data.get('nickname')
    if User.objects.filter(Q(username=username)|Q(nickname=nickname)):
        return Response({"status":"fail"}, status = status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"status":"success"},status=status.HTTP_201_CREATED)