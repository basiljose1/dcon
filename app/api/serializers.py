# from rest_framework import serializers
from rest_witchcraft import serializers

from app.models import LenderEligbl, PilotDealersEligbl, session


class LenderEligblSerializer(serializers.ModelSerializer):

    class Meta:
        model = LenderEligbl
        session = session
        read_only_fields = ('eligbl_id','created_ts')
        fields = ['eligbl_id','created_ts','cp_id', 'st_cd', 'prod_type', 'app_type', 'deal_type',
                  'dt_verification_in', 'incld_in', 'veh_typ_cd', 'modified_by', 'effective_ts']


class PilotDealersEligblSerializer(serializers.ModelSerializer):

    class Meta:
        model = PilotDealersEligbl
        session = session
        fields = '__all__'
