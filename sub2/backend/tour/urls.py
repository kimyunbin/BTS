from django.urls import path
from . import views

app_name = 'tour'

urlpatterns = [

    path('detail/',views.tour_detail, name = 'tour_detail'),
    path('detail/<int:spot_pk>/',views.tour_review, name = 'tour_review')

]