from django.shortcuts import render

# Create your views here.
import requests
from django.http import HttpResponse

# def proxy_image(request, image_url):
#     # 发送 GET 请求获取图片内容
#     response = requests.get(image_url)

#     # 检查请求是否成功
#     if response.status_code == 200:
#         # 将获取到的图片内容返回给前端
#         return HttpResponse(response.content, content_type=response.headers['Content-Type'])
#     else:
#         # 如果请求失败，返回适当的错误消息
#         return HttpResponse("Failed to fetch image", status=response.status_code)

def proxy_image(request, image_url):
    # 构造图片请求
    response = requests.get(image_url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 获取图片的内容类型
        content_type = response.headers.get('Content-Type', 'image/jpeg')
        
        # 返回图片内容给前端
        return HttpResponse(response.content, content_type=content_type)
    else:
        # 如果请求失败，返回错误信息
        return HttpResponse('Failed to fetch image', status=response.status_code)