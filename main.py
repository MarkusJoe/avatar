#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/4/3
# @File Name: main.py


import os
import hashlib
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
from fastapi.responses import RedirectResponse

app = FastAPI()


def check_exists_md5(md5: str):
    """
    Check if the md5 filename exists
    :param md5:
    :return:
    """
    return md5 in os.listdir('./static/')


def generate_md5(content: bytes):
    """
    According to the content generate md5
    :param content:
    :return:
    """
    md5 = hashlib.md5(content).hexdigest()
    return md5


@app.post('/upload/')
async def upload(file: UploadFile = File(...)):
    """
    Upload file
    :param file:
    :return:
    """
    if file.content_type.split('/')[0] != 'image':
        return JSONResponse(content={'code': 400, 'msg': '文件类型错误', 'data': None}, status_code=400)
    res = await file.read()
    md5 = generate_md5(res)
    if check_exists_md5(md5):
        return JSONResponse(content={'code': 400, 'msg': '文件已存在', 'data': f'/avatar/{md5}'}, status_code=400)
    if res == b'':
        return JSONResponse({'code': 400, 'msg': '不要上传空文件', 'data': None}, status_code=400)
    if len(res) >= 1024 * 1024 * 5:
        return JSONResponse({'code': 400, 'msg': '文件过大', 'data': None}, status_code=400)
    with open(f'./static/{md5}', 'wb') as f:
        f.write(res)
    return RedirectResponse(url=f'/avatar/{md5}', status_code=302)


@app.get('/')
@app.post('/')
async def index():
    """
    Index page
    :return:
    """
    return FileResponse('./templates/upload.html', status_code=200)


@app.get('/{md5}/')
@app.post('/{md5}/')
@app.get('/avatar/{md5}/')
@app.post('/avatar/{md5}/')
async def avatar(md5: str, request: Request):
    """
    Avatar page
    :param md5:
    :param request:
    :return:
    """
    filename = md5.split('.')[0]
    if filename not in os.listdir('./static/'):
        return JSONResponse({'code': 404, 'msg': '文件未找到', 'data': None})
    if request.method == 'GET':
        return FileResponse('./static/' + filename)
    return JSONResponse({'code': 200, 'msg': f'/avatar/{filename}', 'data': None})
