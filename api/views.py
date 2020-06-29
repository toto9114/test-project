from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Q

from .models import Profile
from .serializers import ProfileSerializer, ProfileWithLastOrderSerializer, OrderSerializer
from .constants import DEFAULT_SUCCESS_MESSAGE, DEFAULT_FAILED_MESSAGE
from .response_handler import CommonResponse


class SignupView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CommonResponse(status.HTTP_201_CREATED, DEFAULT_SUCCESS_MESSAGE, serializer.data)
        else:
            return CommonResponse(status.HTTP_400_BAD_REQUEST, serializer.errors['error'], {})


# Create your views here.
class ProfileView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().order_by('-created_time')

    def get_queryset(self):
        query_params = self.request.query_params
        name = query_params.get('name')
        email = query_params.get('email')

        queryset = Profile.objects.select_related('user').filter(
            Q(user__username__contains=name if name else '') &
            Q(email__contains=email if email else '')
        )
        return queryset

    def list(self, request, *args, **kwargs):
        data = ProfileWithLastOrderSerializer(self.paginate_queryset(self.get_queryset()), many=True).data
        response = self.get_paginated_response(data)
        return CommonResponse(status.HTTP_200_OK, DEFAULT_SUCCESS_MESSAGE,
                              response.data)

    def retrieve(self, request, *args, **kwargs):
        return CommonResponse(status.HTTP_200_OK, DEFAULT_SUCCESS_MESSAGE,
                              self.get_serializer(self.get_object()).data)


class OrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, profile_id):
        print(request.user)
        try:
            profile = Profile.objects.get(id=profile_id)
            queryset = profile.orders.all()
            return CommonResponse(status.HTTP_200_OK, DEFAULT_SUCCESS_MESSAGE,
                                  OrderSerializer(queryset, many=True).data)
        except Profile.DoesNotExist:
            return CommonResponse(status.HTTP_404_NOT_FOUND, 'profile does not found', {})
