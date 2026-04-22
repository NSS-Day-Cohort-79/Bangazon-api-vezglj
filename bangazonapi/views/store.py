from rest_framework import serializers, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from bangazonapi.models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ("id", "name", "description", "created_date")


class StoreView(ViewSet):

    def list(self, request):
        """
        GET /stores
        Return current user's store (if exists)
        """
        try:
            store = request.user.store
            serializer = StoreSerializer(store, context={"request": request})
            return Response(serializer.data)
        except Store.DoesNotExist:
            return Response(
                {"message": "No store found"}, status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        print("request.data:", request.data)
        print("request.user:", request.user)

        if hasattr(request.user, "store"):
            print("user already has a store")
            return Response(
                {"error": "You already have a store"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        name = request.data.get("name")
        description = request.data.get("description")

        print("name:", name)
        print("description:", description)

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
