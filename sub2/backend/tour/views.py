from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Touristspot,Review
from .serializers import reviewSerializer, tourSerializer
from rest_framework.decorators import api_view
from django.conf import settings
from django.contrib.auth import get_user_model
import jwt

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

    elif request.method =='DELETE':
        '''
        리뷰삭제하기
        '''
        user = finduser(request)
        spot = get_object_or_404(Touristspot, pk = spot_pk)
        review = get_object_or_404(Review, user=user, Touristspot = spot)

