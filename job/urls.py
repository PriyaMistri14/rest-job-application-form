from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = routers.DefaultRouter()
# router.register('user', views.UserViewSet, basename="user")
router.register('candidate', views.CandidateViewSet, basename="candidate")
router.register('academic', views.AcademicViewSet, basename="academic")
router.register('experience', views.ExperienceViewSet, basename="experience")
router.register('language', views.LanguageViewSet, basename="language")
router.register('technology', views.TechnologyViewSet, basename="technology")
router.register('reference', views.ReferenceViewSet, basename="reference")
router.register('preference', views.PreferenceViewSet, basename="preference")


urlpatterns = [
    path('user/',views.UserViewSet.as_view({'get':'list',
    'post':'create'}),name='user'),
    path('job/',include(router.urls)),
    path('api-auth/',include('rest_framework.urls')),
    path('get_token/',TokenObtainPairView.as_view(),name="get_token"),
    path('refresh_token',TokenRefreshView.as_view(),name="refresh_token"),
    path('candidate_list/', views.CandidateList.as_view(), name="candidate_list"),
    path('candidate/', views.candidate_create_view, name="candidate"),
    path('create/', views.CreateCandidateAPIView.as_view(), name="create"),
    path('candidate_create/', views.CandidateCreate.as_view(), name="candidate_create"),
    path('candidate_detail/<int:pk>/', views.CandidateDetail.as_view(), name="candidate_detail"),
]
