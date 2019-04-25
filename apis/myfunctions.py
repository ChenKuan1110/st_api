#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:chenkuan 
# time:2019/4/19

from flask import jsonify, request
from .info import all_apis, info


def get_all_apis():
    """返回所有的api调用接口"""
    return jsonify({'all_apis': all_apis})


def login():
    """处理登陆"""
    username = request.json.get('username')
    password = request.json.get('password')
    if username == "" and password == "":
        return "success"
    return "处理登陆"


def not_found():
    """找不到对应api"""
    return jsonify({'error': "-1"})


def get_info():
    """返回科普文章"""
    return jsonify({"info": info})
