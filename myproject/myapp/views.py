from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# class PostListCreate(APIView):  # 시리얼라이저 쓰기 위한 편한 기능 쓰기 전

#     def get(self, request):
#         return Response({"hello":"world"}, status=200)

#     def post(self, request):
#         p = Post()

#         title = request.data.get("title")
#         p.title = title

#         content = request.data.get("content")
#         p.content = content

#         p.save()
#         return Response({"title": p.title, "content": p.content, "id": p.id})

class PostListCreate(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# class PostRetrieveUpdateDelete(APIView):

#     def get(self, request, id):
#         p = Post.objects.get(id=id)
#         # return Response({"title": p.title, "content": p.content}) # 시리얼라이저 안썼을때
#         return Response(PostSerializer(p).data) # 시리얼라이저 썼을때. 현재 시리얼라이저는 all 옵션이므로 전부 보인다.
    
#     def post(self, request):
#         title = request.data.get("title")
#         if title:
#             return Response({"title":title}, status=200)
#         return Response({}, status=400)

#     def patch(self, request, id): # put은 if문만 빼기. 왜? 패치는 주는 것만 수정이고 풋은 싹 지우고 처음부터 다시 쓰는거니까
#         p = Post.objects.get(id=id)

#         title = request.data.get("title")
#         if title:
#             p.title = title

#         content = request.data.get("content")
#         if content:
#             p.content = content

#         p.save()

#         return Response({"title": p.title, "content": p.content})

#     def delete(self, request, id):
#         p = Post.objects.get(id=id)
#         p.delete()

#         return Response({})

class PostRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    