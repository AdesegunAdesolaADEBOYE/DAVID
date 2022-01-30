from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='created')

    options = (
        ('draft', 'Draft'),
        ('created', 'Created'),
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='created')
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_posts')
    status = models.CharField(max_length=10, choices=options, default='created')
    objects = models.Manager() # default manager
    postobjects = PostObjects() # custom manager

    class Meta:
        ordering = ('-created',)    

    def __str__(self):
        return self.title

