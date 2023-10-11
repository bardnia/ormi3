from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    # main_image = models.ImageField(upload_to='blog/', blank=True, null=True) # upload_to='blog/' : blog 폴더 안에 저장
    main_image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_at.strftime("%Y-%m-%d %H:%M:%S")} : {self.title }'