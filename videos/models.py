from django.db import models

# Create your models here.
class Video(models.Model):

    CATEGORY_CHOICES=[
        (1,'HTML/CSS'),
        (2,'JAVASCRIPT'),
        (3,'PYTHON'),
        (4,'DJANGO')
    ]
    skill_level_CHOICES=[
        (1,'BEGINNER'),
        (2,'INTERMEDIATE'),
        (3,'EXPERT')
    ]
    title=models.CharField(max_length=180,unique=True)
    author=models.CharField(max_length=64)
    discription=models.TextField(unique=True,null=True)
    youtube_vid=models.CharField(max_length=11)
    star_count=models.DecimalField(max_digits=2,decimal_places=1)
    category_id=models.IntegerField(choices=CATEGORY_CHOICES)
    skill_level=models.IntegerField(choices=skill_level_CHOICES)
    is_active=models.BooleanField(default=True)
    posted_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-star_count","title"]

    def __str__(self):
        return self.title+'(' + self.author + ')'



