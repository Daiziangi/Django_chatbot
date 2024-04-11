# # myapp/views.py

# from datetime import timezone
# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import *
# from diffusers import StableDiffusionPipeline
# import torch

# from chatbot.models import Chat as FirstChat

# import random
# from http import HTTPStatus
# import dashscope
# import json

# def text2image(prompt):
#     model_id = "runwayml/stable-diffusion-v1-5"
#     pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
#     pipe = pipe.to("cuda")

#     # prompt = "The bright moonlight shines on the window paper, as if there is a layer of frost on the ground."
#     prompt = "The moonlight before bed, probably on the ground"
#     prompt = prompt+"Semi-realistic style,high quality,China" #Semi-realistic style , Semi-cartoonish style
#     negative_prompt = "low quality,unreally," 
#     image = pipe(prompt,negative_prompt=negative_prompt).images[0]  
#     return image

# dashscope.api_key='sk-4f29b919bd594f2d9d89044babe48a38'
# #定义阿里云API制成的对话AI
# def ask_ali(message):
#     messages = [{'role': 'system', 'content': """你是一个帮助我用于学习英语单词和词组句子等的英语专家,
#                  请耐心帮助我学习和理解并解答我的疑问,并且回答时尽量辅以一些极具画面感的例子."""},
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
#         print(response["output"]["choices"][0]["message"]["content"])
#         pass
#     else:
#         print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
#             response.request_id, response.status_code,
#             response.code, response.message
#         ))
#     return response["output"]["choices"][0]["message"]["content"]

# def chat_with_ai(request):
#     # if request.user.is_authenticated:
#         # try:
#             chats = Chat_En.objects.filter(user_en=request.user)

#             if request.method == 'POST':
#                 message = request.POST.get('message')
#                 response = ask_ali(message)
#                 t2imag_text = response
#                 t2imag_ali2local = call_with_messages(t2imag_text)
#                 image = text2image(t2imag_ali2local)
#                 # chat_first = Chat(user=request.user)
#                 # chat = chat_first.secend_chat
#                 # chat.message = message
#                 # chat.response = response
#                 # chat.image = image
#                 # chat.created_at = timezone.now()
#                 # chat.save()
#                 # chat_first = FirstChat.objects.create(user=request.user)
#                 chat = Chat_En(user_en = request.user ,message=message, response=response, image=image, created_at=timezone.now())
#                 chat.save()
#                 chats = Chat_En.objects.filter(user_en=request.user)
#                 return JsonResponse({'response': response,'image':image,}) 
#             return render(request, 'chatbot_en.html', {'chats': chats})
#         # except Exception as e:
#         #     print("An error occurred:", e)
#         #     return render(request,'login.html')
#     # else:
#     #     return render(request,'login.html')

# #定义阿里云API制成的文生图prompt适配器
# def call_with_messages(message):
#     messages = [{'role': 'system', 'content': """你是一个文生图的prompt适配器,接下来我会将需要进行形象化的内容传递给你,你只需要返回出用于画出对应内容的prompt英文就可以了."""},
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
#         print(response["output"]["choices"][0]["message"]["content"])
#         pass
#     else:
#         print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
#             response.request_id, response.status_code,
#             response.code, response.message
#         ))
#     return response["output"]["choices"][0]["message"]["content"]


