from rest_witchcraft import viewsets
from app.api.serializers import LenderEligblSerializer, PilotDealersEligblSerializer
from app.models import LenderEligbl, PilotDealersEligbl, session

from django.http import JsonResponse


class LenderEligblViewSet(viewsets.ModelViewSet):
    queryset = LenderEligbl.query
    serializer_class = LenderEligblSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.save()
        session.commit()
        return JsonResponse(serializer.instance)


class PilotDealersEligblViewSet(viewsets.ModelViewSet):
    queryset = PilotDealersEligbl.query
    serializer_class = PilotDealersEligblSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.save()
        session.commit()
        return JsonResponse(serializer.instance)