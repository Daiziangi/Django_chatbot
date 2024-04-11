# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.
# from django.db import models

# class ChatContent(models.Model):
#     message = models.TextField()
#     response = models.TextField()
#     conclusion = models.TextField()

# class Chat(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content_consume = models.ForeignKey(ChatContent, related_name='chat_content_consume', on_delete=models.CASCADE)
#     id_content = models.ForeignKey(ChatContent, related_name='chat_content_id', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='generated_images/', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)



from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    # image_url = models.URLField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='generated_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.
# from django.db import models

# class ChatContent(models.Model):
#     message = models.TextField()
#     response = models.TextField()
#     conclusion = models.TextField()

# class Chat(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content_consume = models.ForeignKey(ChatContent, related_name='chat_content_consume', on_delete=models.CASCADE)
#     id_content = models.ForeignKey(ChatContent, related_name='chat_content_id', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='generated_images/', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)



from django.db import models
from django.contrib.auth.models import User
from chatbot.models import Chat as FirstChat
# Create your models here.
class Chat_En(models.Model):
    user_en = models.ForeignKey(User,related_name='chat_en', on_delete=models.CASCADE)
    # first_chat = models.OneToOneField(FirstChat, on_delete=models.CASCADE, related_name='second_chat')
    message = models.TextField()
    response = models.TextField()
    image = models.ImageField(upload_to='generated_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'