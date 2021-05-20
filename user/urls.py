from django.urls import path
from .views import MyObtainTokenPairView, RegisterView, UserList, UserDetail
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', RegisterView.as_view(), name='auth_register'),
    path('list/', UserList.as_view()),
    path('list/<int:pk>', UserDetail.as_view()),
]

