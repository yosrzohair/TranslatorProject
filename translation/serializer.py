from rest_framework import serializers

class TranslatoionReqSerializer(serializers.Serializer):
    text = serializers.CharField()
    target_language = serializers.CharField()