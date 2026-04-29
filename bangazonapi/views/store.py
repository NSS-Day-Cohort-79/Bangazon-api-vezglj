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

        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication required"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if Store.objects.filter(owner=request.user).exists():
            return Response(
                {
                    "non_field_errors": [
                        "You already have a store and cannot create another one."
                    ]
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        name = request.data.get("name", "").strip()
        description = request.data.get("description", "").strip()

        errors = {}

        if not name:
            errors["name"] = ["Store name is required."]

        if not description:
            errors["description"] = ["Store description is required."]

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

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
