from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .tasks import user_update_asynchronous
import threading


# Create your views here.
@api_view(['POST'])
def signup(request):
    serializer: UserSerializer = UserSerializer(data=request.data, context={'request': request})

    if serializer.is_valid():
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        threading.Thread(target=user_update_asynchronous, args=[user.id], daemon=True).start()
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# @permission_classes([IsAuthenticated]) Use this for authentication for functions
def greeting(request):
    return Response("Heloo....", status=status.HTTP_201_CREATED)


class UserDetailsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user