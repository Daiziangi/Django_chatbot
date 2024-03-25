from django.shortcuts import render

# Create your views here.
import requests
from django.http import HttpResponse


def proxy_image(request, image_url):
    try:
        # 获取远程图片内容
        response = requests.get(image_url)
        if response.status_code == 200:
            content_type = response.headers.get('Content-Type', 'image/jpeg')
            # 返回图片内容给前端
            return HttpResponse(response.content, content_type=content_type)
    except Exception as e:
        # 处理异常情况
        pass
    # 如果获取失败，返回空白图片或其他提示信息
    return HttpResponse(status=404)