from api.models import Buyer
from marshmallow import Schema, fields, post_load, validates, ValidationError
from collections import namedtuple
from arrow import arrow

import datetime as dt
NewBuyer = namedtuple('PeopleData', [
    'id',
    'name',
    'time',
])

class NewPersonSchema(Schema):
    person_name = fields.String(required=True)
    person_id = fields.String(required=True)
    time = fields.DateTime(required=False)

    @post_load
    def new_buyer(self, data):
        return NewBuyer(**data)
    
    @validates('person_name')
    def validates_name(self, value):
        if not value:
            raise ValidationError("Buyer's name must be known")
    
    @validates('person_id')
    def validates_buyer_id(self, value):
        if not value:
            raise ValidationError('The Buyer must have na ID')
    
    @validates('time')
    def validates_time(self , value):
        try:
            # arrow.get(value).datetime
            isinstance(value, str)
        except Exception as e:
            print(e)
            raise Exception('The time of transaction must be known')     
