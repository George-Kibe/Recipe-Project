"""Recipe API serializers"""

from rest_framework import serializers

from core.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe objects"""

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'time_minutes', 'price', 'link')
        read_only_fields = ('id',)

class RecipeDetailSerializer(RecipeSerializer):
    """Serialize a recipe detail"""
    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ('description',)
    # ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())
    # time_minutes = serializers.IntegerField(read_only=True)
    # price = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
    # link = serializers.URLField(read_only=True)
    # tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())
    # title = serializers.CharField(read_only=True)