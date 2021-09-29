from botocore.retries import bucket
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Review, Route, RouteTouristspot, Routelike, ToruistImg, Touristspot, RouteTouristspot
from .serializers import reviewSerializer, tourSerializer, RouteSerializer, RouteTouristspotSerializer,PhotoSerializer
from rest_framework.decorators import api_view
from django.conf import settings
from django.contrib.auth import get_user_model
import jwt
from accounts.models import City
from accounts.serializers import CitySerializer
# Create your views here.

def finduser(request):
    token = request.headers['Authorization'].split()[1]
    SECRET_KEY = settings.SECRET_KEY
    payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    user = get_object_or_404(get_user_model(), username=payload["username"])
    return user

@api_view(('GET',))
def tour_detail(request):
    '''
    지역코드를 path_variable로 받는다. 
    부산광역시, 시흥시, 서울특별시등 xx시로 받는다.
    지역의 관광지,문화시설,레포츠,숙박,음식을 리뷰순으로 정렬하여 20개 반환한다. 
    '''
    code = request.GET.get('code')
    print(code)
    

    views = Touristspot.objects.filter(address__icontains=code,category='관광지').order_by('-counting')[:20]
    cultures = Touristspot.objects.filter(address__icontains=code,category='문화시설').order_by('-counting')[:20]
    eats = Touristspot.objects.filter(address__icontains=code,category='음식').order_by('-counting')[:20]
    sleeps = Touristspot.objects.filter(address__icontains=code,category='숙박').order_by('-counting')[:20]
    reports = Touristspot.objects.filter(address__icontains=code,category='레포츠').order_by('-counting')[:20]

    view = tourSerializer(data=views, many=True)
    culture = tourSerializer(data=cultures, many=True)
    report = tourSerializer(data=reports, many=True)
    sleep = tourSerializer(data=sleeps, many=True)
    eat = tourSerializer(data=eats, many=True)


    print(view.is_valid(), culture.is_valid(), report.is_valid(), sleep.is_valid(), eat.is_valid())
    context = {
        '관광지': view.data,
        '문화시설': culture.data,
        '음식':report.data,
        '숙박': sleep.data,
        '레포츠':eat.data
    }
    return Response(context)

@api_view(['GET','POST'])
def tour_review(request, spot_pk):
    if request.method =='GET':
        review = Review.objects.filter(Touristspot = spot_pk)

        serialer = reviewSerializer(data = review, many= True)
        print(serialer.is_valid())

        context ={
            'review': serialer.data
        }
        return Response(context)
    elif request.method =='POST':
        '''
        리뷰 생성 
        '''
        rating = request.data.get('rating')
        content = request.data.get('content')
        user = finduser(request)
        spot = get_object_or_404(Touristspot, pk = spot_pk)
        review = Review(user=user, Touristspot = spot, rating=rating, content=content)
        review.save()
        return Response({"status":"success"}, status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def route(request):
    user = finduser(request)
    if request.method == 'POST':
        route = Route(title=request.data['title'], user=user)
        route.save()
        for s in request.data['spot']:
            spot = get_object_or_404(Touristspot, title = s)
            temp = RouteTouristspot(route=route, touristspot=spot)
            temp.save()
        return Response({"status":"success"})
    elif request.method == 'GET':
        route = get_list_or_404(Route, user=user)

        return Response(RouteSerializer(route, many=True).data)
@api_view(('GET',))
def tour_city(request):
    man = [32030, 37020, 39020, 31370, 34030, 32060, 39010, 36020, 37010, 21090, 34380, 32010, 38090, 38050, 38350, 31380, 35380, 35020, 36310, 35010, 34020, 38080, 33380, 35330, 31200, 23310, 23010, 21140, 34370, 38100]
    woman = [39020, 37020, 32030, 39010, 32060, 21090, 31370, 34030, 31380, 35010, 37010, 34380, 36020, 38350, 32010, 38050, 38090, 36310, 23310, 31270, 35020, 31200, 35380, 33380, 34020, 38100, 35330, 38080, 31240, 32410]
    single = [39020, 31010, 32030, 21090, 36020, 37010, 39010, 34080, 35380, 32060, 38050, 38080, 22020, 31240, 34020, 31090, 38100, 37020, 36390, 31370, 36350, 26310, 25050, 36470, 21050, 34370, 21010, 34030, 31220, 34360]
    multi = [39020, 37020, 32030, 39010, 31370, 32060, 34030, 21090, 37010, 36020, 34380, 32010, 31380, 38090, 38350, 35010, 38050, 36310, 35020, 35380, 23310, 34020, 33380, 31200, 35330, 38080, 31270, 23010, 38100, 31240]
    poor = [23080, 11090, 37370, 31160, 31170, 11130, 31040, 11100, 37100, 11120, 37390, 38320, 29010, 31110, 22310, 22050, 11080, 33390, 21120, 31120, 25050, 33330, 37070, 31100, 34310, 33370, 31260, 31080, 31020, 31030]
    rich = [39010, 39020, 37430, 21060, 22040, 11180, 21130, 32060, 32340, 32410, 11250, 32350, 32400, 32030, 21090, 36020, 21020, 32390, 32330, 32070, 38090, 38050, 32310, 36470, 11240, 32040, 34380, 22020, 37420, 35340]
    family = [23080, 11120, 25010, 37370, 11030, 37100, 31170, 21120, 33350, 25050, 37390, 31160, 38320, 34070, 29010, 11220, 31110, 22050, 31120, 11080, 31070, 31040, 34310, 31100, 38330, 34020, 37050, 22020, 31220, 31010]
    friend = [37370, 11170, 11090, 31040, 36430, 31170, 37080, 11130, 31160, 33390, 31080, 11210, 11100, 37100, 37320, 22310, 23080, 11120, 38320, 31260, 37390, 37070, 29010, 31140, 26310, 11080, 31110, 31030, 31050, 25010]

    user = finduser(request)
    genders = user.sex
    travelers = user.travelers
    budgets = user.budget
    companions = user.companion
    if genders == True :
        gender = City.objects.filter(code__in = man,user=user).order_by('-satis')[:10]
    else:
        gender = City.objects.filter(code__in = woman,user=user).order_by('-satis')[:10]

    if travelers == 1:
        traveler = City.objects.filter(code__in =single,user=user).order_by('-satis')[:10]
    else :
        traveler = City.objects.filter(code__in =multi,user=user).order_by('-satis')[:10]
    
    if budgets <= 100000:
        budget = City.objects.filter(code__in =poor,user=user).order_by('-satis')[:10]
    else:
        budget = City.objects.filter(code__in =rich,user=user).order_by('-satis')[:10]

    if companions == True:
        companion = City.objects.filter(code__in =family,user=user).order_by('-satis')[:10]
    elif companions == False:
        companion = City.objects.filter(code__in =friend,user=user).order_by('-satis')[:10]
    else:
        companion = City.objects.filter(code__in =single,user=user).order_by('-satis')[:10]

    genderserializer = CitySerializer(data=gender, many=True)
    travelerserializer = CitySerializer(data=traveler, many=True)
    budgetserializer = CitySerializer(data=budget, many=True)
    companionserializer = CitySerializer(data=companion, many=True)

    print(genderserializer.is_valid(),travelerserializer.is_valid(),budgetserializer.is_valid(),companionserializer.is_valid())
    
    context = {
        'gender': genderserializer.data,
        'traveler' : travelerserializer.data,
        'budget': budgetserializer.data,
        'companion': companionserializer.data,
    }
    return Response(context)
    # return Response({"context":genderserializer.data})

import requests
from PIL import Image
@api_view(('POST',))
def test(request):
    img=ToruistImg.objects.get(id=1)
    url = 'https:' +img.images
    img_response = requests.get(url)

    # print(img_response.content)
    if img_response.status_code == 200:
        #print(img_response.content)
    
        print("========= [이미지 저장] =========")
        with open('test.jpg', 'wb') as fp:
            fp.write(img_response.content)
        image = Image.open("test.jpg")
        print(image)
    test = {
        'image': image,
        'testfield': 's'
    }
    
    serializer = PhotoSerializer(data = test)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

