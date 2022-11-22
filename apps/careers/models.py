from django.db import models
from apps.commons.models import NameDescModel
from .constants import JOB_TYPE_Choices, WORK_TYPE_Choices

# # Create your models here.
# class DemoModel(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.PositiveIntegerField()


# Create your models here.
# Job or Career Model
class CareerInfoModel(models.Model):
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
    work_type = models.CharField(max_length=20, blank=True, choices = WORK_TYPE_Choices) #help_text="signifies if the job is remote or office"
    submission_deadline = models.DateField()

    def __str__(self):
        return f"{self.job_title} ---->> {self.submission_deadline}"

    class Meta:
        verbose_name = 'Career Information Model'
        verbose_name_plural = 'Career Information Models'


# Apply Career Common Model for both published jobs and unpublished jobs (drop your cv part)
class ApplyCareerCommonModel(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    cover_letter = models.TextField(blank=True)
    cv = models.FileField(upload_to='cv/')
    yrs_of_experience = models.CharField(max_length=50)

    class Meta:
        abstract = True


# Career Apply Model Form
class CareerApplyModel(ApplyCareerCommonModel):
    career = models.ForeignKey(CareerInfoModel, on_delete=models.SET_NULL, blank=True, null=True)
    current_salary = models.CharField(max_length=10)
    expected_salary = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.full_name} applies for  {self.career.job_title}"

    class Meta:
        verbose_name = 'Career Apply Model'
        verbose_name_plural = 'Career Apply Models'


# Drop your CV Model
class CVCareerModel(ApplyCareerCommonModel):
    area_of_expertise = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_Choices) # signifies if he/she applies for internship or work or Freelancing

    def __str__(self):
        return f"{self.full_name} is searching for {self.area_of_expertise} as {self.job_type}"

    class Meta:
        verbose_name = 'CV Career Apply Model'
        verbose_name_plural = 'CV Career Apply Models'
