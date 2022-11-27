from django.db import models
from apps.commons.models import NameDescModel, BaseUUIDModel
from .constants import JOB_TYPE_CHOICES, WORK_TYPE_CHOICES, GENDER_CHOICES


# Create your models here.
# Job or Career Model
class Career(BaseUUIDModel):
    job_title = models.CharField(max_length=150)
    job_req = models.TextField(help_text="Job Requirements", blank=True)
    quantity = models.CharField(max_length=20, blank=True,
                                help_text="Number of employees required")
    job_role = models.TextField(help_text="Job Responsibilities", blank=True)
    category = models.CharField(max_length=50, null=True,
                                help_text="signifies if job category is design or development or graphics or any")
    experience = models.CharField(max_length=50, blank=True)
    job_location = models.CharField(max_length=50, blank=True)
    salary = models.CharField(max_length=25, blank=True)
    work_type = models.CharField(max_length=20, blank=True, choices=WORK_TYPE_CHOICES) #help_text="signifies if the job is remote or office"
    submission_deadline = models.DateField()

    def __str__(self):
        return f"{self.job_title}"

    class Meta:
        verbose_name = 'Career'
        verbose_name_plural = 'CareerS'


# Apply Career Common Model for both published jobs and unpublished jobs (drop your cv part)
class ApplicantDataAbstractModel(BaseUUIDModel):
    full_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100, null=True, blank=True)
    cover_letter = models.TextField(blank=True)
    cv = models.FileField(upload_to='cv/')
    yrs_of_experience = models.CharField(max_length=50)

    class Meta:
        abstract = True


# Career Apply Model Form
class Applicant(ApplicantDataAbstractModel):
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='job_listed')
    current_salary = models.CharField(max_length=10)
    expected_salary = models.CharField(max_length=10)

    @property
    def display_name(self):
        return f"{self.full_name}"

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Applicant'
        verbose_name_plural = 'Applicants'


# Drop your CV Model
class DropCVModel(ApplicantDataAbstractModel):
    area_of_expertise = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES) # signifies if he/she applies for internship or work or Freelancing

    def __str__(self):
        return f"{self.full_name} is searching for {self.area_of_expertise} as {self.job_type}"

    class Meta:
        verbose_name = 'Drop Your CV Model'
        verbose_name_plural = 'Drop Your CV Models'
