# myapp/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import Dialog

def add_dialog(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')  # 获取用户提交的对话内容
        if content:
            # 将对话内容保存到数据库中
            dialog = Dialog.objects.create(content=content)
            response_data = {'success': True, 'message': '对话已新增', 'dialog_id': dialog.id}
        else:
            response_data = {'success': False, 'message': '对话内容不能为空'}
    else:
        response_data = {'success': False, 'message': '仅支持POST请求'}
    return JsonResponse(response_data)


from .models import Message

def send_message(request):
    if request.method == 'POST':
        message_content = request.POST.get('message', '')  # 获取用户输入的消息内容
        if message_content:
            # 在这里处理发送消息的逻辑，比如将消息保存到数据库中
            message = Message.objects.create(content=message_content)
            # 假设发送消息成功
            response_data = {'success': True, 'message': '消息已发送', 'data': {'message_id': message.id, 'message': message_content}}
        else:
            response_data = {'success': False, 'message': '消息内容不能为空'}
    else:
        response_data = {'success': False, 'message': '请求方法不允许'}
    return JsonResponse(response_data)

from .models import BrowseHistory

def index(request):
    # 从数据库中获取最近浏览的记录
    browsing_history = BrowseHistory.objects.all().order_by('-timestamp')[:5]

    return render(request, 'chat_english.html', {'browsing_history': browsing_history})



import random
from http import HTTPStatus
import dashscope
import json
dashscope.api_key='sk-4f29b919bd594f2d9d89044babe48a38'
#定义阿里云API制成的对话AI
def call_with_messages(message):
    messages = [{'role': 'system', 'content': """你是一个帮助我用于学习英语单词和词组句子等的英语专家,请耐心帮助我学习和理解并解答我的疑问."""},
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

def chat_with_ai(request):
    if request.method == 'POST':
        # 获取用户发送的消息内容
        user_message = request.POST.get('message', '')

        # 调用 AI 模型与用户对话
        response_message = call_with_messages(user_message)

        # 将 AI 模型的响应返回给用户
        return JsonResponse({'success': True, 'message': response_message})

    else:
        return JsonResponse({'success': False, 'message': '请求方法不允许'}, status=405)

# #定义阿里云API制成的文生图prompt适配器
# def call_with_messages(message):
#     messages = [{'role': 'system', 'content': """你是一个文生图的prompt适配器,接下来我会将需要进行形象化的内容传递给你,你只需要返回出用于画出对应内容的prompt就可以了."""},
#                 {'role': 'user', 'content': message}]
#     response = dashscope.Generation.call(
#         "qwen-turbo",
#         messages=messages,
#         # set the random seed, optional, default to 1234 if not set
#         seed=random.randint(1, 10000),
#         # set the result to be "message" format.
#         result_format='message',
#     )
#     if response.status_code == HTTPStatus.OK:
#         # print(response)
#         pass
#     else:
#         print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
#             response.request_id, response.status_code,
#             response.code, response.message
#         ))
#     return response["output"]["choices"][0]["message"]["content"]


