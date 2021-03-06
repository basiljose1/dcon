from rest_witchcraft import viewsets
from app.api.serializers import LenderEligblSerializer, PilotDealersEligblSerializer
from app.models import LenderEligbl, PilotDealersEligbl, session

from django.http import JsonResponse


class LenderEligblViewSet(viewsets.ModelViewSet):
    queryset = LenderEligbl.query
    serializer_class = LenderEligblSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            session.commit()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors)


class PilotDealersEligblViewSet(viewsets.ModelViewSet):
    queryset = PilotDealersEligbl.query
    serializer_class = PilotDealersEligblSerializer

    def create(self, request):
        eligbl_id = request.data.pop('eligbl_id')
        eligbl_se = LenderEligblSerializer(data=eligbl_id)
        eligbl_se.is_valid()
        eligbl_se.save()
        data = request.data
        data['eligbl_id'] = eligbl_se.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            session.commit()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors)