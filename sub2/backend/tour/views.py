from django.shortcuts import render
from rest_framework.response import Response
from .models import Touristspot
from .models import Review
from .serializers import reviewSerializer, tourSerializer
# Create your views here.
from rest_framework.decorators import api_view

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

@api_view(('GET',))
def tour_review(request, review_pk):

    review = Review.objects.filter(Touristspot = review_pk)

    serialer = reviewSerializer(data = review, many= True)
    print(serialer.is_valid())

    context ={
        'review': serialer.data
    }
    return Response(context)
