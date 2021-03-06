from django.http.response import JsonResponse
from rest_framework.serializers import Serializer
from tour.models import Touristspot,Review
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserCreateSerializer, CitySerializer, UserLoginSerializer, WishSerialzer
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404
from django.conf import settings
from .models import User, City,WishList

import jwt
import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from django.db.models import Q
from django.db.models import Avg
from accounts import serializers
citys = [11010, 11020, 11030, 11040, 11050, 11060, 11080, 11090, 11100, 11110, 11120, 11130, 11140, 11150, 11160, 11170, 11180, 11190, 11210, 11220, 11230, 11240, 11250, 21010, 21020, 21030, 21040, 21050, 21060, 21070, 21080, 21090, 21100, 21110, 21120, 21130, 21140, 21310, 22010, 22020, 22040, 22050, 22060, 22070, 22310, 23010, 23020, 23030, 23040, 23050, 23060, 23070, 23080, 23310, 23320, 24010, 24020, 24030, 24040, 24050, 25010, 25020, 25030, 25040, 25050, 26010, 26020, 26030, 26040, 26310, 29010, 31010, 31020, 31030, 31040, 31050, 31060, 31070, 31080, 31090, 31100, 31110, 31120, 31130, 31140, 31150, 31160, 31170, 31180, 31190, 31200, 31210, 31220, 31230, 31240, 31250, 31260, 31270, 31280, 31350, 31370, 31380, 32010, 32020, 32030, 32040, 32050, 32060, 32070, 32310, 32320, 32330, 32340, 32350, 32360, 32370, 32390, 32400, 32410, 33020, 33030, 33040, 33320, 33330, 33340, 33350, 33360, 33370, 33380, 33390, 34010, 34020, 34030, 34040, 34050, 34060, 34070, 34080, 34310, 34330, 34340, 34350, 34360, 34370, 34380, 35010, 35020, 35030, 35040, 35050, 35060, 35310, 35320, 35330, 35340, 35350, 35360, 35370, 35380, 36010, 36020, 36030, 36040, 36060, 36310, 36320, 36330, 36350, 36360, 36370, 36380, 36390, 36400, 36410, 36420, 36430, 36440, 36450, 36460, 36470, 36480, 37010, 37020, 37030, 37040, 37050, 37060, 37070, 37080, 37090, 37100, 37310, 37320, 37330, 37340, 37350, 37360, 37370, 37380, 37390, 37400, 37410, 37420, 37430, 38030, 38050, 38060, 38070, 38080, 38090, 38100, 38110, 38310, 38320, 38330, 38340, 38350, 38360, 38370, 38380, 38390, 38400, 39010, 39020]
ages = [19,25,27,34,41,54,68,73]
state_city = {'11010':'??????????????? ?????????', '11020':'??????????????? ??????', '11030':'??????????????? ?????????','11040':'??????????????? ?????????','11050':'??????????????? ?????????','11060':'??????????????? ????????????','11070':'??????????????? ?????????','11080':'??????????????? ?????????','11090':'??????????????? ?????????','11100':'??????????????? ?????????','11110':'??????????????? ?????????','11120':'??????????????? ?????????','11130':'??????????????? ????????????','11140':'??????????????? ?????????','11150':'??????????????? ?????????','11160':'??????????????? ?????????','11170':'??????????????? ?????????','11180':'??????????????? ?????????','11190':'??????????????? ????????????','11200':'??????????????? ?????????','11210':'??????????????? ?????????','11220':'??????????????? ?????????','11230':'??????????????? ?????????','11240':'??????????????? ?????????','11250':'??????????????? ?????????','21010':'??????????????? ??????','21020':'??????????????? ??????','21030':'??????????????? ??????','21040':'??????????????? ?????????','21050':'??????????????? ????????????','21060':'??????????????? ?????????','21070':'??????????????? ??????','21080':'??????????????? ??????','21090':'??????????????? ????????????','21100':'??????????????? ?????????','21110':'??????????????? ?????????','21120':'??????????????? ?????????','21130':'??????????????? ?????????','21140':'??????????????? ?????????','21150':'??????????????? ?????????','21310':'??????????????? ?????????','22010':'??????????????? ??????','22020':'??????????????? ??????','22030':'??????????????? ??????','22040':'??????????????? ??????','22050':'??????????????? ??????','22060':'??????????????? ?????????','22070':'??????????????? ?????????', '22310':'??????????????? ?????????','23010':'??????????????? ??????','23020':'??????????????? ??????','23030':'??????????????? ????????????','23040':'??????????????? ?????????','23050':'??????????????? ?????????','23060':'??????????????? ?????????','23070':'??????????????? ?????????','23080':'??????????????? ??????','23090':'??????????????? ????????????','23310':'??????????????? ?????????','23320':'??????????????? ?????????','24010':'??????????????? ??????','24020':'??????????????? ??????','24030':'??????????????? ??????','24040':'??????????????? ??????','24050':'??????????????? ?????????','25010':'??????????????? ??????','25020':'??????????????? ??????','25030':'??????????????? ??????','25040':'??????????????? ?????????','25050':'??????????????? ?????????','26010':'??????????????? ??????','26020':'??????????????? ??????', '26030':'??????????????? ??????','26040':'??????????????? ??????','26310':'??????????????? ?????????','29010':'????????????????????? ?????????????????????','31010':'????????? ?????????','31020':'????????? ?????????','31030':'????????? ????????????','31040':'????????? ?????????','31050':'????????? ?????????','31060':'????????? ?????????','31070':'????????? ?????????','31080':'????????? ????????????','31090':'????????? ?????????','31100':'????????? ?????????','31110':'????????? ?????????','31120':'????????? ?????????','31130':'????????? ????????????','31140':'????????? ?????????','31150':'????????? ?????????','31160':'????????? ?????????','31170':'????????? ?????????','31180':'????????? ?????????','31190':'????????? ?????????','31200':'????????? ?????????','31210':'????????? ?????????','31220':'????????? ?????????','31230':'????????? ?????????','31240':'????????? ?????????','31250':'????????? ?????????','31260':'????????? ?????????','31270':'????????? ?????????','31280':'????????? ?????????','31350':'????????? ?????????','31370':'????????? ?????????','31380':'????????? ?????????','32010':'????????? ?????????','32020':'????????? ?????????','32030':'????????? ?????????','32040':'????????? ?????????','32050':'????????? ?????????','32060':'????????? ?????????','32070':'????????? ?????????','32310':'????????? ?????????', '32320':'????????? ?????????','32330':'????????? ?????????','32340':'????????? ?????????','32350':'????????? ?????????','32360':'????????? ?????????','32370':'????????? ?????????','32380':'????????? ?????????','32390':'????????? ?????????','32400':'????????? ?????????','32410':'????????? ?????????','33020':'???????????? ?????????','33030':'???????????? ?????????','33040':'???????????? ?????????','33320':'???????????? ?????????','33330':'???????????? ?????????','33340':'???????????? ?????????','33350':'???????????? ?????????','33360':'???????????? ?????????','33370':'???????????? ?????????','33380':'???????????? ?????????','33390':'???????????? ?????????','34010':'???????????? ?????????','34020':'???????????? ?????????','34030':'???????????? ?????????','34040':'???????????? ?????????','34050':'???????????? ?????????','34060':'???????????? ?????????','34070':'???????????? ?????????','34080':'???????????? ?????????','34310':'???????????? ?????????','34330':'???????????? ?????????','34340':'???????????? ?????????','34350':'???????????? ?????????','34360':'???????????? ?????????','34370':'???????????? ?????????','34380':'???????????? ?????????','35010':'???????????? ?????????','35020':'???????????? ?????????','35030':'???????????? ?????????','35040':'???????????? ?????????','35050':'???????????? ?????????','35060':'???????????? ?????????','35310':'???????????? ?????????','35320':'???????????? ?????????','35330':'???????????? ?????????','35340':'???????????? ?????????','35350':'???????????? ?????????', '35360':'???????????? ?????????','35370':'???????????? ?????????','35380':'???????????? ?????????','36010':'???????????? ?????????','36020':'???????????? ?????????','36030':'???????????? ?????????','36040':'???????????? ?????????','36060':'???????????? ?????????','36310':'???????????? ?????????','36320':'???????????? ?????????','36330':'???????????? ?????????','36350':'???????????? ?????????','36360':'???????????? ?????????','36370':'???????????? ?????????','36380':'???????????? ?????????','36390':'???????????? ?????????','36400':'???????????? ?????????','36410':'???????????? ?????????','36420':'???????????? ?????????','36430':'???????????? ?????????','36440':'???????????? ?????????','36450':'???????????? ?????????','36460':'???????????? ?????????','36470':'???????????? ?????????','36480':'???????????? ?????????','37010':'???????????? ?????????','37020':'???????????? ?????????','37030':'???????????? ?????????','37040':'???????????? ?????????','37050':'???????????? ?????????','37060':'???????????? ?????????','37070':'???????????? ?????????','37080':'???????????? ?????????','37090':'???????????? ?????????','37100':'???????????? ?????????','37310':'???????????? ?????????','37320':'???????????? ?????????','37330':'???????????? ?????????','37340':'???????????? ?????????','37350':'???????????? ?????????','37360':'???????????? ?????????','37370':'???????????? ?????????','37380':'???????????? ?????????', '37390':'???????????? ?????????','37400':'???????????? ?????????','37410':'???????????? ?????????','37420':'???????????? ?????????','37430':'???????????? ?????????','38030':'???????????? ?????????','38050':'???????????? ?????????','38060':'???????????? ?????????','38070':'???????????? ?????????','38080':'???????????? ?????????','38090':'???????????? ?????????','38100':'???????????? ?????????','38110':'???????????? ?????????','38310':'???????????? ?????????','38320':'???????????? ?????????','38330':'???????????? ?????????','38340':'???????????? ?????????','38350':'???????????? ?????????','38360':'???????????? ?????????','38370':'???????????? ?????????','38380':'???????????? ?????????','38390':'???????????? ?????????','38400':'???????????? ?????????','39010':'????????????????????? ?????????','39020':'????????????????????? ????????????',}
man = [32030, 37020, 39020, 31370, 34030, 32060, 39010, 36020, 37010, 21090, 34380, 32010, 38090, 38050, 38350, 31380, 35380, 35020, 36310, 35010, 34020, 38080, 33380, 35330, 31200, 23310, 23010, 21140, 34370, 38100]
woman = [39020, 37020, 32030, 39010, 32060, 21090, 31370, 34030, 31380, 35010, 37010, 34380, 36020, 38350, 32010, 38050, 38090, 36310, 23310, 31270, 35020, 31200, 35380, 33380, 34020, 38100, 35330, 38080, 31240, 32410]
single = [39020, 31010, 32030, 21090, 36020, 37010, 39010, 34080, 35380, 32060, 38050, 38080, 22020, 31240, 34020, 31090, 38100, 37020, 36390, 31370, 36350, 26310, 25050, 36470, 21050, 34370, 21010, 34030, 31220, 34360]
multi = [39020, 37020, 32030, 39010, 31370, 32060, 34030, 21090, 37010, 36020, 34380, 32010, 31380, 38090, 38350, 35010, 38050, 36310, 35020, 35380, 23310, 34020, 33380, 31200, 35330, 38080, 31270, 23010, 38100, 31240]
poor = [23080, 11090, 37370, 31160, 31170, 11130, 31040, 11100, 37100, 11120, 37390, 38320, 29010, 31110, 22310, 22050, 11080, 33390, 21120, 31120, 25050, 33330, 37070, 31100, 34310, 33370, 31260, 31080, 31020, 31030]
rich = [39010, 39020, 37430, 21060, 22040, 11180, 21130, 32060, 32340, 32410, 11250, 32350, 32400, 32030, 21090, 36020, 21020, 32390, 32330, 32070, 38090, 38050, 32310, 36470, 11240, 32040, 34380, 22020, 37420, 35340]
family = [23080, 11120, 25010, 37370, 11030, 37100, 31170, 21120, 33350, 25050, 37390, 31160, 38320, 34070, 29010, 11220, 31110, 22050, 31120, 11080, 31070, 31040, 34310, 31100, 38330, 34020, 37050, 22020, 31220, 31010]
friend = [37370, 11170, 11090, 31040, 36430, 31170, 37080, 11130, 31160, 33390, 31080, 11210, 11100, 37100, 37320, 22310, 23080, 11120, 38320, 31260, 37390, 37070, 29010, 31140, 26310, 11080, 31110, 31030, 31050, 25010]


def userSatis(request,user):
    budget, travelers, companion, transportation, selection, age, activity = int(request.data.get('budget')), int(request.data.get('travelers')), request.data.get('companion'), request.data.get('transportation'), request.data.get('selection'), request.data.get('age'), request.data.get('activity')
    forest = joblib.load(os.path.join(os.path.dirname(os.path.dirname(__file__)),'bigdata/forest.pkl'))
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
        s, c = state_city[str(citys[i])].split()
        cityObject = City(user=user, city=c, state=s, satis=temp, code=citys[i])
        cityObject.save()
        

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserCreateSerializer(data=request.data)
    print('---')
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        userSatis(request,user)
        return Response({"status":"success"}, status=status.HTTP_201_CREATED)
    return Response({"status":"fail"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    serializer = UserLoginSerializer(data=request.data)
    if not serializer.is_valid(raise_exception=True):
        return Response({"status":"Request Body Error."}, status=status.HTTP_409_CONFLICT)
    if serializer.validated_data['username'] == "None":
        return Response({"status": "fail"}, status=status.HTTP_200_OK)
    response = {
        'success':True,
        'token':serializer.data['token'],
        'nickname': serializer.data['nickname']
    }
    return Response(response, status=status.HTTP_200_OK)

@api_view(['POST'])
def checkusername(request):
    '''
    ?????? ????????? ??? ????????? ???????????? 
    '''
    username = request.data.get('username')
    nickname = request.data.get('nickname')
    if User.objects.filter(Q(username=username)|Q(nickname=nickname)):
        return Response({"status":"fail"}, status = status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"status":"success"},status=status.HTTP_201_CREATED)

import requests
@api_view(['POST'])
def usertest(request):
    
    url = 'https://img1.kakaocdn.net/relay/local/R640x320/?fname=http%3A%2F%2Fcfile27.uf.tistory.com%2Fimage%2F99C9B2465BC59E95178EDA'
        #?????? url??? ???????????? ??????
    img_response = requests.get(url)

    #????????? ???????????????,
    if img_response.status_code == 200:
        #print(img_response.content)
    
        print("========= [????????? ??????] =========")
        with open("test.jpg", "wb") as fp:
            fp.write(img_response.content)

    return Response({"status":"ss"})
@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommendcity(request):
    token = request.headers['Authorization'].split()[1]
    SECRET_KEY = settings.SECRET_KEY
    payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    user = get_object_or_404(User, username=payload["username"])
    print(user.sex)
    print(user.travelers)
    print(user.budget)
    print(user.companion)
    city = get_list_or_404(City.objects.order_by('-satis'),user=user.pk)
    serializer = CitySerializer(city, many=True)
    for i in range(22):
        serializer.data[i]['score']=10
    for i in range(22,44):
        serializer.data[i]['score']=9
    for i in range(44,66):
        serializer.data[i]['score']=8
    for i in range(66,88):
        serializer.data[i]['score']=7
    for i in range(88,110):
        serializer.data[i]['score']=6
    for i in range(110,132):
        serializer.data[i]['score']=5
    for i in range(132,154):
        serializer.data[i]['score']=4
    for i in range(154,176):
        serializer.data[i]['score']=3
    for i in range(176,198):
        serializer.data[i]['score']=2
    for i in range(198,224):
        serializer.data[i]['score']=1
    return Response({'main':[{'title':'personal','country':serializer.data}]}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def follow(request,tour_id):
    '''
    userid??? jwt??? spot_id ??? url??? ?????????. 
    ???????????? ???????????? whishlist?????? ????????? ??????
    ????????? ???????????? ????????? ?????????.  
    '''
    token = request.headers['Authorization'].split()[1]
    SECRET_KEY = settings.SECRET_KEY
    payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    user = get_object_or_404(User, username=payload["username"])
    tour = Touristspot.objects.get(pk=tour_id)
    if WishList.objects.filter(user=user,Touristspot=tour).exists():
        WishList.objects.filter(user=user,Touristspot=tour).delete()
        follow = False
    else:
        WishList.objects.create(user=user,Touristspot=tour)
        follow = True

    return Response({"status":follow }, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def wishlist(request):
    
    token = request.headers['Authorization'].split()[1]
    SECRET_KEY = settings.SECRET_KEY
    payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    user = get_object_or_404(User, username=payload["username"])
    
    if not WishList.objects.filter(user=user).exists():
        return Response({"data": [] },status=status.HTTP_200_OK)
    
    wishlist = get_list_or_404(WishList,user=user)
    
    serializers = WishSerialzer(data=wishlist, many=True)

    print(serializers.is_valid())

    context = {
        'data': serializers.data,
        
    }
    return Response(context,status=status.HTTP_200_OK)
