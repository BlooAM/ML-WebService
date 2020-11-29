from rest_framework import mixins, viewsets

from backend.server.apps.endpoints.models import Endpoint, MLAlgorithm, MLAlgorithmStatus, MLRequest
from backend.server.apps.endpoints.serializers import EndpointSerializer, MLAlgorithmSerializer, \
    MLAlgorithmStatusSerializer, MLRequestSerializer


class EndpointViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = EndpointSerializer
    queryset = Endpoint.objects.all()


class MLAlgorithmViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = MLAlgorithmSerializer
    queryset = MLAlgorithm.objects.all()