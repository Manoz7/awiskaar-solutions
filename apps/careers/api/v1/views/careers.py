from django.shortcuts import render
#
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser
from rest_framework.generics import get_object_or_404


#
from apps.commons.mixins.viewsets import ListCreateUpdateRetrieveViewSetMixin, DestroyViewSetMixin

from ..serializer.careers import CareerSerializer, ApplicantSerializer, DropCVSerializer
from apps.careers.models import Career, Applicant, DropCVModel


class CareerViewSet(ListCreateUpdateRetrieveViewSetMixin, DestroyViewSetMixin):
    queryset = Career.objects.all()
    permission_classes = AllowAny,
    lookup_field = 'uuid'
    lookup_kwarg = 'uuid'

    def get_serializer_class(self):
        if self.action == 'apply':
            return ApplicantSerializer
        return CareerSerializer

    @action(detail=True, methods=['post'], url_path='apply', url_name='apply-job')
    def apply(self, request, *args, **kwargs):
        self.parser_classes = [FileUploadParser]
        obj = self.get_object()
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        obj.job_posted.create(**ser.validated_data)
        return Response(
            {"detail": f"{ser.validated_data} Job applied successfully."}
        )

    @action(methods=['get'], detail=True, url_path='applicants', url_name='applicants-lists')
    def applicants(self, request, *args, **kwargs):
        obj = self.get_object()
        ser = ApplicantSerializer(obj.job_listed.all(), many=True)
        return Response(ser.data)

    @action(methods=['delete'], detail=True, url_path='delete_applicant', url_name='delete-applicants')
    def delete_applicant(self, request, *args, **kwargs):
        applicant = get_object_or_404(
            Applicant,
            uuid=self.kwargs.get('uuid')
        )
        applicant.delete()
        return Response(
            {'detail': 'Applicant deleted successfully.'}
        )

class DropCVViewSet(ListCreateUpdateRetrieveViewSetMixin, DestroyViewSetMixin):
    permission_classes = AllowAny,
    serializer_class = DropCVSerializer
    lookup_field = 'uuid'
    lookup_kwarg = 'uuid'
    queryset = DropCVModel.objects.all()


# class ApplicantViewSet(ListCreateUpdateRetrieveViewSetMixin):
#     queryset = Applicant.objects.all()
#     permission_classes = AllowAny,
#     lookup_field = 'uuid'
#     lookup_kwarg = 'uuid'
#     serializer_class = CareerSerializer

