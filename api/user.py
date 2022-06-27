# -*- coding: utf-8 -*-
"""
Copyright (c) XYZ Robotics Inc. - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Author: tingting ge <tingting.ge@xyzrobotics.ai>, Date: 27/06/22
"""
from flask import request
from flask_restful import Resource
from marshmallow import fields, Schema, ValidationError
from libs import ResponseCode as Rc


class User(Resource):
    def __init__(self):
        pass

    def get(self):
        data = {
            'name': 'tina',
            'age': 18
        }
        return Rc(data_=data).success()
