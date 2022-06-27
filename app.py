#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) XYZ Robotics Inc. - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Author: tingting ge <tingting.ge@xyzrobotics.ai>, Date: 25/06/22
"""

from threading import Lock
from flask import Flask, request, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS  # 跨域请求用的
from flask_restful import Api
import json
from utils import router_exception_checker

from api import Test, User

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
api = Api(app, decorators=[router_exception_checker])
socketio = SocketIO(app, cors_allowed_origins="*")

thread_lock = Lock()


@app.route('/')
def echo_alive():
    return jsonify({'echo': 'alive'})


@socketio.on('connect')
def establish_sockio():
    global is_background_thread_alive

    with thread_lock:
        if not is_background_thread_alive:
            is_background_thread_alive = True

    print('Client connected')


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


api.add_resource(Test, '/api/test')
api.add_resource(User, '/api/user')

# @app.route('/http/query/', methods=['post'])
# def post_http():
#     if not request.data:  # 检测是否有数据
#         return ('fail')
#     params = request.data.decode('utf-8')
#     # 获取到POST过来的数据，因为我这里传过来的数据需要转换一下编码。根据晶具体情况而定
#     prams = json.loads(params)
#     print(prams)
#     # 把区获取到的数据转为JSON格式。
#     return jsonify(prams)
#     # 返回JSON数据。


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
