# from rest_framework import serializers
from rest_witchcraft import serializers

from app.models import LenderEligbl, PilotDealersEligbl, session


class LenderEligblSerializer(serializers.ModelSerializer):

    class Meta:
        model = LenderEligbl
        session = session
        read_only_fields = ('eligbl_id','created_ts')
        fields = '__all__'

class PilotDealersEligblSerializer(serializers.ModelSerializer):

    class Meta:
        model = PilotDealersEligbl
        session = session
        fields = '__all__'
