from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer




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
        # print(user.password)
    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
    return Response( {"status": "success"},status=status.HTTP_201_CREATED)
