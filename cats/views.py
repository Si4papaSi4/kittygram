from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Cat
from .serializers import CatSerializer


class APICat(APIView):
    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CatSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APICatDetail(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cat = get_object_or_404(Cat, id=kwargs.get('pk'))
    def get(self, request, **kwargs):
        serializer = CatSerializer(self.cat)
        return Response(serializer.data)

    def put(self, request, **kwargs):
        serializer = CatSerializer(self.cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        return self.put(request)

    def delete(self, request, **kwargs):
        self.cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



