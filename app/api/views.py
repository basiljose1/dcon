from rest_witchcraft import viewsets
from app.api.serializers import LenderEligblSerializer, PilotDealersEligblSerializer, PilotDealersEligblSerializer1
from app.models import LenderEligbl, PilotDealersEligbl, session
from django.http import JsonResponse
from rest_framework.response import Response


class LenderEligblViewSet(viewsets.ModelViewSet):
    queryset = LenderEligbl.query
    serializer_class = LenderEligblSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            session.commit()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class PilotDealersEligblViewSet(viewsets.ModelViewSet):
    queryset = PilotDealersEligbl.query
    serializer_class = PilotDealersEligblSerializer

    def create(self, request):
        lender = LenderEligbl.query.filter_by(eligbl_id=request.data.get('eligbl_id')).first()
        pilot = PilotDealersEligbl(dlr_id=request.data.get('dlr_id'),eligbl_id=lender)
        session.commit()
        return Response({"dlr_id":pilot.dlr_id,"eligbl_id":pilot.eligbl_id.eligbl_id})

    def list(self, request):
        queryset = PilotDealersEligbl.query.all()
        serializer = PilotDealersEligblSerializer1(queryset, many=True)
        return Response(serializer.data)