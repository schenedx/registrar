"""
The public-facing REST API.
"""
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from registrar.apps.enrollments import api
from registrar.apps.enrollments import data
from registrar.apps.enrollments.models import (
    Learner,
    LearnerProgramEnrollment,
    Program,
)
from registrar.apps.api.serializers import (
    LearnerProgramEnrollmentSerializer,
    ProgramSerializer,
)


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    lookup_field = 'discovery_uuid'
    serializer_class = ProgramSerializer

    def retrieve(self, request, discovery_uuid):
        program = self.get_object()
        return Response(program)

    def create(self, request):
        discovery_uuid = request.data.pop('discovery_uuid', None)
        try:
            existing_program = Program.objects.get(discovery_uuid=discovery_uuid)
            return Response(existing_program)
        except Program.DoesNotExist:
            program_from_discovery = data.get_discovery_program(discovery_uuid)
            if not program_from_discovery:
                raise
            program_from_discovery.update(request.data)
            new_program, _ = api.update_or_create_program(discovery_uuid, program_from_discovery)
            return Response(new_program)


class ProgramEnrollmentView(APIView):
    def get(self, request, discovery_uuid=None, learner_id=None):
        if discovery_uuid:
            enrollments = LearnerProgramEnrollment.objects.filter(program__discovery_uuid=discovery_uuid)
            return Response(LearnerProgramEnrollmentSerializer(enrollments, many=True).data)

    def post(self, request, discovery_uuid):
        try:
            program = Program.objects.get(discovery_uuid=discovery_uuid)
        except Program.DoesNotExist:
            # automagically create it for them, if it exists in discovery?
            return Response({'sweet': 'nothin'})

        emails = request.data.pop('emails')
        for email in emails:
            try:
                learner = Learner.objects.get(email=email)
            except Learner.DoesNotExist:
                learner, was_created = api.update_or_create_learner(email)
                if was_created:
                    lms_user = data.get_lms_user_by_email(email)
                    if lms_user:
                       lms_user = lms_user[0] 
                       learner.lms_id = lms_user['id']
                       learner.save()

            enrollment, _ = api.enroll_in_program(learner=learner, program=program)
        return Response({'status': 'ok'})
