from rest_framework.views import APIView
from rest_framework.response import Response

class PostRetriveUpdate(APIView):

    def get(self, request):
        return Response({"hello":"world"}, status=200)

    def post(self, request):
        title = request.data.get("title")
        if title:
            return Response({"title":title}, status=200)
        return Response({}, status=400)