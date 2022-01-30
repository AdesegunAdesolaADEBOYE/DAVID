from rest_framework import generics
from event.models import Post
from .serializers import PostSerializer

# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass


class PostDetail(generics.RetrieveDestroyAPIView):
    pass
