"""
The public-facing REST API.
"""
from rest_framework import viewsets
from rest_framework.response import Response

from registrar.apps.enrollments import api as enrollments_api
from registrar.apps.enrollments.models import Program
from registrar.apps.api.serializers import ProgramSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    lookup_field = 'discovery_uuid'
    serializer_class = ProgramSerializer

    def retrieve(self, request, discovery_uuid):
        program = self.get_object()
        return Response(program)

    def create(self, request):
        pass


class ProgramEnrollmentViewSet(viewsets.ModelViewSet):
    pass
