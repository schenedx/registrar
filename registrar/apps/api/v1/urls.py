""" API v1 URLs. """
from rest_framework import routers

from .views import ProgramViewSet

router = routers.SimpleRouter()
router.register(r'programs', ProgramViewSet, basename='Program')

urlpatterns = router.urls
