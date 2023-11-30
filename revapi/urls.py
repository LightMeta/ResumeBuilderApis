from django.urls import path
from .views import CandidateProfileViewSet, MultiCandidateDataViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('candidate_info', CandidateProfileViewSet, basename='candidate_view')
# router.register('candidate_bulk_insert',MultiCandidateDataViewSet,basename='multicandidate_view')

urlpatterns = [
    path('bulk_insert/',MultiCandidateDataViewSet.as_view())
]

urlpatterns += router.urls