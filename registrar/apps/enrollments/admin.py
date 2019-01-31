""" Admin configuration for enrollments models. """
from django.contrib import admin

from registrar.apps.enrollments import models



admin.site.register(models.CourseRun)
admin.site.register(models.Learner)
admin.site.register(models.LearnerCourseRunEnrollment)
admin.site.register(models.LearnerProgramEnrollment)
admin.site.register(models.Organization)
admin.site.register(models.OrganizationProgramMembership)
admin.site.register(models.Program)
