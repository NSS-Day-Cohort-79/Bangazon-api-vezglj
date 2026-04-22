from rest_framework import serializers, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from bangazonapi.models import Store, stores


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ("id", "name", "description", "created_date")


class StoreView(ViewSet):

    def list(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication required"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if Store.objects.filter(owner=request.user).exists():
            return Response(
                {"error": "You already have a store"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        name = request.data.get("name")
        description = request.data.get("description")

        if not name or not description:
            return Response(
                {"error": "Name and description are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        new_store = Store.objects.create(
            owner=request.user, name=name, description=description
        )

        serializer = StoreSerializer(new_store, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
