from typing import Any
from django.contrib.auth import get_user_model
from rest_framework import generics, response, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from app.user.models import Profile
from app.user.permissions import IsUser
from app.user.serializers import (
    LogoutSerializer,
    PasswordResetSerializer,
    ProfileSerializer,
    UserSerializer,
    VerifyEmailSerializer,
    VerifyPasswordResetSerializer,
)

User = get_user_model()


class UserRegister(APIView):
    def post(self, request: Request, format: str = "json") -> Response:
        serializer = UserSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        response = serializer.data
        response["refresh"] = str(refresh)
        response["access"] = str(refresh.access_token)

        return Response(response, status=status.HTTP_201_CREATED)


class VerifyEmailView(GenericAPIView):
    serializer_class = VerifyEmailSerializer

    def patch(
        self, request: Request, encoded_pk: str, token: str, **kwargs: str
    ) -> Response:
        data = {"encoded_pk": encoded_pk, "token": token}

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Email verified", status=status.HTTP_200_OK)


class LogoutView(GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (IsAuthenticated,)

    def post(self, request):  # type:ignore[no-untyped-def]

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        IsUser,
    )
    serializer_class = ProfileSerializer
    lookup_field = "user"
    queryset = Profile.objects.all()


class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)


class PasswordReset(generics.GenericAPIView):
    """
    Request for Password Reset Link.
    """

    serializer_class = PasswordResetSerializer

    def post(self, request: Request, format: str = "json") -> Response:

        serializer = self.get_serializer(
            data={"email": request.data.get("email")}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {"message": "Check your email for the password reset link"},
            status=status.HTTP_200_OK,
        )


class VerifyPasswordReset(generics.GenericAPIView):

    serializer_class = VerifyPasswordResetSerializer

    def post(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        """
        Verify token & encoded_pk and then reset the password.
        """
        serializer = self.get_serializer(
            data=request.data, context={"kwargs": kwargs}
        )

        serializer.is_valid(raise_exception=True)

        return response.Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )
    