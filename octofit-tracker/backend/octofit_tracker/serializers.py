from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard
from bson import ObjectId


class ObjectIdModelSerializer(serializers.ModelSerializer):
    """Base serializer that converts ObjectId instances to strings for JSON compatibility."""

    def _convert_objectid(self, value):
        if isinstance(value, ObjectId):
            return str(value)
        if isinstance(value, dict):
            return {key: self._convert_objectid(val) for key, val in value.items()}
        if isinstance(value, list):
            return [self._convert_objectid(item) for item in value]
        if isinstance(value, tuple):
            return tuple(self._convert_objectid(item) for item in value)
        return value

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return self._convert_objectid(data)


class UserSerializer(ObjectIdModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TeamSerializer(ObjectIdModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class ActivitySerializer(ObjectIdModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class WorkoutSerializer(ObjectIdModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class LeaderboardSerializer(ObjectIdModelSerializer):
    class Meta:
        model = Leaderboard
        fields = '__all__'
