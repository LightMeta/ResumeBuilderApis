from rest_framework import viewsets
from .serializers import CandidateSerializer
from .models import Candidate
from rest_framework.response import Response
from rest_framework.views import APIView
import django_filters
from .utils.createpdf import CreatePdf


class CandidateProfileViewSet(viewsets.ModelViewSet):

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def create(self, request):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            create_pdf_object = CreatePdf(request.data)
            create_pdf_object.create_pdf()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class MultiCandidateDataViewSet(APIView):
    serializerclass = CandidateSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get(self,request):
        all_objects = Candidate.objects.all()
        serializer = CandidateSerializer(all_objects, many=True)
        return Response(serializer.data)


    def post(self, request):
        data = request.data
        if not data:
            return Response({

                                'status':False,
                                'message': 'Kindly insert some data'

                            })
        
        candidates_data = data['candidates']
        serializer = self.serializerclass(data=candidates_data, many=True)
        if serializer.is_valid():
            serializer.save()
            
            for each_input in candidates_data:
                create_pdf_object = CreatePdf(each_input)
                create_pdf_object.create_pdf()
            return Response({
                'status': True,
                'message': 'Candidates saved successfully'
            })
        else:
            return Response({
                'status': False,
                'message': serializer.errors
            })
