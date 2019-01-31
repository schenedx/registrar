"""
Models relating to learner program and course enrollments.
"""
from django.db import models
from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords


class Organization(TimeStampedModel):
    """
    Model that represents a course-discovery Organization entity.
    """
    discovery_uuid = models.UUIDField(db_index=True, null=True)
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)


class Program(TimeStampedModel):
    """
    Table that referrences a course-discovery Program entity.
    """
    class Meta(object):
        app_label = 'enrollments'

    discovery_uuid = models.UUIDField(db_index=True, null=True)
    title = models.CharField(max_length=255)
    organizations = models.ManyToManyField(
        Organization,
        related_name='programs',
        through='OrganizationProgramMembership'
    )


class OrganizationProgramMembership(TimeStampedModel):
    """
    Table that captures the relationship between Programs and Organizations.
    """
    class Meta(object):
        app_label = 'enrollments'
        unique_together = [
            ('program', 'organization',)
        ]

    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    history = HistoricalRecords()


class Learner(TimeStampedModel):
    """
    Model that represents an LMS user who may be enrolled in programs and courses.
    """
    PENDING = 'pending'
    ACCOUNT_CREATED = 'account_created'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (ACCOUNT_CREATED, 'Account Created'),
    )

    lms_id = models.IntegerField(db_index=True, null=True)

    # for storing id field provided by org
    external_id = models.CharField(max_length=255, db_index=True, null=True)

    email = models.EmailField(db_index=True)
    status = models.CharField(
        max_length=64,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    history = HistoricalRecords()


class LearnerProgramEnrollment(TimeStampedModel):
    """
    Model that represents the relationship between a Learner and a Program.
    """
    PENDING = 'pending'
    ENROLLED = 'enrolled'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (ENROLLED, 'Enrolled'),
    )

    # we shouldn't be able to delete any of these fields out from under
    # ourselves if an enrollment record is using them.
    learner = models.ForeignKey(Learner, on_delete=models.PROTECT)
    program = models.ForeignKey(Program, on_delete=models.PROTECT)
    status = models.CharField(
        max_length=64,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    history = HistoricalRecords()


class CourseRun(TimeStampedModel):
    """
    Model that represents a course-discovery CourseRun entity.
    """
    discovery_uuid = models.UUIDField(db_index=True, null=True)
    title = models.CharField(max_length=512)
    key = models.CharField(max_length=255, db_index=True)


class LearnerCourseRunEnrollment(TimeStampedModel):
    """
    Respresents the fact of a learner being enrolled in a course run.
    """
    PENDING = 'pending'
    ENROLLED = 'enrolled'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (ENROLLED, 'Enrolled'),
    )

    learner = models.ForeignKey(Learner, on_delete=models.PROTECT)
    course_run = models.ForeignKey(CourseRun, on_delete=models.PROTECT)
    status = models.CharField(
        max_length=64,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    history = HistoricalRecords()
