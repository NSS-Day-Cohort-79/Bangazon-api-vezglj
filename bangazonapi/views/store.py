from rest_framework import serializers, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from bangazonapi.models import Store, stores
from bangazonapi.views import user


class StoreSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = ("id", "name", "description", "created_date", "seller")

    def get_seller(self, obj):
        owner = getattr(obj, "owner", None)

        if not owner:
            return {
                "first_name": "",
                "last_name": "",
            }

        return {
            "first_name": getattr(owner, "first_name", ""),
            "last_name": getattr(owner, "last_name", ""),
        }


class StoreView(ViewSet):

    def list(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        print("request.data:", request.data)
        print("request.user:", request.user)

        if not request.user.is_authenticated:
            return Response(
                {"error": "Authentication required"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if Store.objects.filter(owner=request.user).exists():
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

    def retrieve(self, request, pk=None):
        try:
            store = Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            return Response(
                {"error": "Store not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = StoreSerializer(store, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
