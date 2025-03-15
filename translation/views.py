from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializer import TranslatoionReqSerializer
from .service import TranslationService

class TranslationReqView(APIView):
    def post(self , request):
        data = request.data
        serializer = TranslatoionReqSerializer(data = data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            target_language = serializer.validated_data['target_language']
            
            
            try:
                translated_data = TranslationService.translate_text(text , target_language)
                return Response(translated_data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error:" f"Error Happened: {str(e)}"} , status=status.HTTP_400_BAD_REQUEST)
        return Response (serializer.errors , status=status.HTTP_400_BAD_REQUEST)
