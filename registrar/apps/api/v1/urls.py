""" API v1 URLs. """
from django.conf.urls import url
from rest_framework import routers

from .views import ProgramEnrollmentView, ProgramViewSet


urlpatterns = [
    url(
        r'programs/enrollment/(?P<discovery_uuid>[0-9A-Fa-f\-]+)/$',
        ProgramEnrollmentView.as_view(),
        name='program-enrollments'
    ),
]

router = routers.SimpleRouter()
router.register(r'programs', ProgramViewSet, basename='Program')

urlpatterns += router.urls
