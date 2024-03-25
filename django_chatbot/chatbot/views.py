from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from django.utils import timezone

import os
from django.core.files.base import ContentFile
import base64


import json
import requests

openai_api_key = 'sk-wCTF9hG5g6h4lyU6COKEQP0WwRRsXowkaiXPtbmGX5iw6UBa'
openai.api_key = openai_api_key


API_KEY = "zrpJizLeTwQ3plXyhvV2RoBw"
SECRET_KEY = "ZdRKOqJzMEr5pZmJJnnmv29xcYkfAr2X"
def baidu_chat(message):
        
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-speed-128k?access_token=" + get_access_token()
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ],
        "system": "你是一个中国古代诗词专家及教师,接下来请帮助我理解和记忆各个诗词和古文"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    # print(response.text)
    res = response.json()["result"]
    # print(res)
    return res

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


def ask_baidu(message):
    dialog = baidu_chat(message)
    return dialog


def chatbot(request):
    if request.user.is_authenticated:
        try:
            chats = Chat.objects.filter(user=request.user)

            if request.method == 'POST':
                message = request.POST.get('message')
                response = ask_baidu(message)
                t2imag_baidu2ali = response
                t2imag_ali2zhipu = call_with_messages(t2imag_baidu2ali)
                image_url = zhipu(t2imag_ali2zhipu)
                chat = Chat(user=request.user, message=message, response=response, image_url=image_url,created_at=timezone.now())
                chat.save()
                print("Image URL:", chat.image_url)
                meta_refresh = '<meta http-equiv="refresh" content="45">'  # 提交表单后自动刷新页面，延迟时间为45秒
                return JsonResponse({'message': message, 'response': response,'image_url':image_url,})
            return render(request, 'chatbot.html', {'chats': chats})
        except Exception as e:
            print("An error occurred:", e)
            return render(request,'index.html')
    else:
        return render(request,'index.html')


import random
from http import HTTPStatus
import dashscope
import json
dashscope.api_key='sk-4f29b919bd594f2d9d89044babe48a38'
#定义阿里云API制成的文生图prompt适配器
def call_with_messages(message):
    messages = [{'role': 'system', 'content': """你是一个文生图的prompt适配器,接下来我会将中国古代文化内容传递给你,你需要从中提取出可以形象化表现我传递于你的内容的文生图prompt,并只返回给我对应的prompt.
                 (如果发给你的是人物则要求能够画出其画像,如果是诗词语句则能够形象化地表现出其中的内容和场景). 请强烈注意,请直接返回给我对应用于文生图的prompt里的内容,不要包含其他任何东西(包括如'prompt'和'文生图prompt'的字样)"""},
                {'role': 'user', 'content': message}]
    response = dashscope.Generation.call(
        "qwen-turbo",
        messages=messages,
        # set the random seed, optional, default to 1234 if not set
        seed=random.randint(1, 10000),
        # set the result to be "message" format.
        result_format='message',
    )
    if response.status_code == HTTPStatus.OK:
        # print(response)
        pass
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
    return response["output"]["choices"][0]["message"]["content"]





from zhipuai import ZhipuAI
def zhipu(ali_prompt):
    client = ZhipuAI(api_key="752c820e46b49c524f1397eb4cb23728.0OM9RWz0OAK0uaxJ") # 请填写您自己的APIKey

    response = client.images.generations(
        model="cogview-3", #填写需要调用的模型名称
        prompt=ali_prompt,
    )
    # print(response.data[0].url)
    return response.data[0].url





def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
