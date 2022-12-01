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


class ListUpdateRetrieveViewSetMixin(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    pass


class RetrieveDestroyViewSetMixin(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    pass


class ListRetrieveDestroyViewSetMixin(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    pass


class ListCreateRetrieveDestroyViewSetMixin(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    pass
