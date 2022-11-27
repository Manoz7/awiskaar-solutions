from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ListCreateRetrieveViewSetMixin(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    pass


class ListCreateUpdateViewSetMixin(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    pass


class ListCreateUpdateRetrieveViewSetMixin(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    pass


class DestroyViewSetMixin(
    mixins.DestroyModelMixin
):
    pass
