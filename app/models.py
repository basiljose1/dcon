# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
import sqlalchemy as sa
import sqlalchemy.orm  # noqa
from sqlalchemy.ext.declarative import declarative_base

# default - PostgreSQL
# engine = sa.create_engine('postgresql://scott:tiger@localhost/mydatabase')

# default - mysql
engine = sa.create_engine('mysql://root:root@localhost/dcon')


# default - oracle
# engine = sa.create_engine('oracle://scott:tiger@127.0.0.1:1521/sidname')

# sqlite
# engine = sa.create_engine('sqlite:///foo.db', echo=True)

session = sa.orm.scoped_session(sa.orm.sessionmaker(bind=engine))

Base = declarative_base()
Base.query = session.query_property()


class LenderEligbl(Base):
    __tablename__ = 'dcon_lender_eligbl'

    eligbl_id = sa.Column(sa.Integer(), primary_key=True, autoincrement=True)
    cp_id = sa.Column(sa.Integer(), nullable=False)
    st_cd = sa.Column(sa.String(20))
    prod_type = sa.Column(sa.String(20), nullable=False)
    app_type = sa.Column(sa.String(20), nullable=False, default='I')
    deal_type = sa.Column(sa.String(20), nullable=False)
    dt_verification_in = sa.Column(sa.String(20), nullable=False)
    incld_in = sa.Column(sa.String(20), nullable=False, default='Y')
    veh_typ_cd = sa.Column(sa.String(20))
    created_ts = sa.Column(sa.DateTime(), default=datetime.datetime.utcnow)
    updtd_ts = sa.Column(sa.DateTime(), default=datetime.datetime.utcnow)
    modified_by = sa.Column(sa.String(20))
    effective_ts = sa.Column(sa.DateTime())


class PilotDealersEligbl(Base):
    __tablename__ = 'pilot_dealers_eligbl'

    id = sa.Column(sa.Integer(), primary_key=True, autoincrement=True)
    dlr_id = sa.Column(sa.Integer())

    _eligbl_id = sa.Column('eligbl_id', sa.Integer(),
                           sa.ForeignKey('dcon_lender_eligbl.eligbl_id'))
    eligbl_id = sa.orm.relationship(LenderEligbl, backref='dcon_lender_eligbl')
    __table_args__ = (sa.UniqueConstraint('dlr_id', 'eligbl_id', name='_dlr_eligbl_uc'),
                     )

Base.metadata.create_all(engine)
