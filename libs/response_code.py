# -*- coding: utf-8 -*-
"""
Copyright (c) XYZ Robotics Inc. - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Author: tingting ge <tingting.ge@xyzrobotics.ai>, Date: 25/06/22
"""
class ResponseCode:
    def __init__(self, id_=None, data_=None, msg_=None, type_=None, action_=None, path_=None):

        self.id = id_
        self.data = data_
        self.msg = msg_
        self.type = type_
        self.action = action_
        self.path = path_

    def success(self):
        body = {
            'code': 200,
            'msg': "Operation succeeded",
            'id': self.id,
            'data': self.data
        }
        return body

    def unknown_error(self):
        body = {
            'code': -1,
            'msg': "Operation failed.",
            'id': self.id,
            'data': self.data
        }
        return body

    def workspace_key_error(self):
        body = {
            'code': -2,
            'msg': "Can not find work space.",
            'id': self.id,
            'data': self.data
        }
        return body

    def camera_key_error(self):
        body = {
            'code': -2,
            'msg': "Can not find camera.",
            'id': self.id,
            'data': self.data
        }
        return body

    def path_not_found(self):
        body = {
            'code': -3,
            'msg': "Profile does not exist.",
            'id': self.id,
            'data': self.data,
            'type': 'environment'
        }
        if self.path:
            body['msg'] = self.path + ' does not exist'
        return body

    def service_error(self):
        body = {
            'code': -4,
            'msg': "Service error.",
            'id': self.id,
            'data': self.data
        }
        return body

    def request_error(self):
        body = {
            'code': -5,
            'msg': "Request error.",
            'id': self.id,
            'data': self.data
        }
        return body

    def package_key_error(self):
        body = {
            'code': -6,
            'msg': "Can not find configuration package.",
            'id': self.id,
            'data': self.data
        }
        return body

    def network_error(self):
        body = {
            'code': -7,
            'msg': "Can not connect to the Internet.",
            'id': self.id,
            'data': self.data
        }
        return body

    def annotation_key_error(self):
        body = {
            'code': -8,
            'msg': "annotation key error in vision config",
            'id': self.id,
            'data': self.data
        }
        return body

    def part_picking_bridge_error(self):
        body = {
            'code': -9,
            'msg': "part picking bridge error",
            'id': self.id,
            'data': self.data
        }
        return body

    def grippers_key_error(self):
        body = {
            'code': -10,
            'msg': "grippers key error in vision config",
            'id': self.id,
            'data': self.data
        }
        return body

    def object_placing_error(self):
        body = {
            'code': -11,
            'msg': "object is not in correct tote",
            'id': self.id,
            'data': self.data
        }
        return body

    def customized_error(self):
        body = {
            'code': -500,
            'msg': self.msg,
            'id': self.id,
            'data': self.data,
            'type': self.type,
            'action': self.action,
        }
        return body

    def part_picking_error(self):
        body = {
            'code': -500,
            'msg': self.msg,
            'id': self.id,
            'data': self.data,
            'type': 'part_picking',
            'action': self.action,
        }
        return body

    def calibration_error(self):
        body = {
            'code': -500,
            'msg': self.msg,
            'id': self.id,
            'data': self.data,
            'type': 'calibration',
            'action': self.action,
        }
        return body

    def vision_sensor_error(self):
        body = {
            'code': -500,
            'msg': self.msg,
            'id': self.id,
            'data': self.data,
            'type': 'vision_sensor',
            'action': self.action,
        }
        return body
