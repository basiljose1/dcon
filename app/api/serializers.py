# from rest_framework import serializers
from rest_witchcraft import serializers

from rest_framework import serializers as sers

from app.models import LenderEligbl, PilotDealersEligbl, session


class LenderEligblSerializer(serializers.ModelSerializer):

    class Meta:
        model = LenderEligbl
        session = session
        read_only_fields = ('eligbl_id','created_ts')
        fields = '__all__'

class PilotDealersEligblSerializer1(serializers.ModelSerializer):

    class Meta:
        model = PilotDealersEligbl
        session = session
        fields = ['dlr_id','eligbl_id']

class PilotDealersEligblSerializer(serializers.ModelSerializer):

    lendersp = LenderEligbl.query.filter(LenderEligbl.incld_in.in_(['P'])).all()

    choices = [(i.eligbl_id,'-'.join([i.app_type,i.st_cd,i.prod_type,i.deal_type,i.dt_verification_in,i.incld_in,i.veh_typ_cd,i.modified_by])) for i in lendersp]

    eligbl_id = sers.ChoiceField(choices=choices)

    class Meta:
        model = PilotDealersEligbl
        session = session
        fields = ['dlr_id','eligbl_id']
