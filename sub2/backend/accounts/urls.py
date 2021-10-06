from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login , name ='login'), # login jwt 토큰 발급
    path('check/',views.checkusername, name='checkusername'),
    path('recommendcity/',views.recommendcity),
    path('follow/<int:tour_id>/',views.follow, name='follow'), # 위시리스트 저장
    path('wishlist/',views.wishlist,name='wishlist'),
    path('usertest/',views.usertest),
    

]