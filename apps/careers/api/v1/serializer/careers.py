from rest_framework import serializers
from apps.commons.serializers import DynamicFieldsModelSerializer
from apps.careers.models import Career, Applicant, DropCVModel


class CareerSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Career
        fields = ('uuid', 'job_title', 'job_req', 'quantity', 'job_role', 'category', 'experience',
                  'job_location', 'salary', 'work_type', 'submission_deadline')


class DropCVSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = DropCVModel
        fields = ['uuid', 'full_name',  'email', 'phone_number', 'location', 'cover_letter', 'cv',
                  'yrs_of_experience', 'area_of_expertise', 'job_type']


class ApplicantSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Applicant
        fields = ('uuid', 'full_name',  'email', 'phone_number', 'cover_letter', 'cv',
                  'yrs_of_experience', 'current_salary', 'expected_salary')
