from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.renderers import TemplateHTMLRenderer
from .models import CandidateMaster
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,CandidateSerializer,AcademicSerialiazer,ExperienceSerialiazer,LanguageSerialiazer,TechnologySerialiazer,ReferenceSerialiazer,PreferenceSerialiazer
from rest_framework.decorators import api_view
from .models import User,CandidateMaster,AcademicMaster,ExperienceMaster,LanguageKnownMaster,TechnologyKnownMaster,ReferenceMaster,PreferenceMaster
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer





class CandidateViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CandidateMaster.objects.all()
    serializer_class = CandidateSerializer


class AcademicViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = AcademicMaster.objects.all()
    serializer_class = AcademicSerialiazer



class ExperienceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ExperienceMaster.objects.all()
    serializer_class = ExperienceSerialiazer




class LanguageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = LanguageKnownMaster.objects.all()
    serializer_class = LanguageSerialiazer




class TechnologyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = TechnologyKnownMaster.objects.all()
    serializer_class = TechnologySerialiazer





class ReferenceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ReferenceMaster.objects.all()
    serializer_class = ReferenceSerialiazer



class PreferenceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = PreferenceMaster.objects.all()
    serializer_class = PreferenceSerialiazer





class CreateCandidateAPIView(generics.CreateAPIView):
    serializer_class = CandidateSerializer

class CreateAcademicAPIView(generics.CreateAPIView):
    serializer_class = AcademicSerialiazer




@api_view(['GET','POST'])
def candidate_create_view(request):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'candidate_create_view.html'
    if request.method == "GET":
        demo = CandidateMaster.objects.all()
        serializer = CandidateSerializer(demo, many=True)
        data= serializer.data
        return Response(data, template_name="candidate_create_view.html")
        # return render(request,"candidate_create_view.html")
        # return Response({'serializer':serializer.data})
    elif request.method == 'POST':
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data, template_name="candidate_create_view.html")
            # return render(request, "candidate_create_view.html")
            # return Response(serializer.data)
        return Response({'serializer':serializer.errors})



# Create your views here.

class CandidateList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name= 'candidate_list_view.html'

    def get(self,request):
        queryset = CandidateMaster.objects.all()
        return Response({'candidates':queryset})
    def post(self,request):
        renderer_classes = [TemplateHTMLRenderer]
        template_name = 'candidate_create_view.html'
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('candidate_list')

        return Response({'serializer': serializer})




class CandidateCreate(APIView):

    # def get(self,request):
    #     renderer_classes = [TemplateHTMLRenderer]
    #     template_name = 'candidate_create_view.html'
    #     return Response({'serializer': serializer})


    def post(self,request):
        renderer_classes = [TemplateHTMLRenderer]
        template_name = 'candidate_create_view.html'
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('candidate_list')

        return Response({'serializer': serializer})






class CandidateDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='candidate_detail_view.html'

    def get(self,request,pk):
        candidate= get_object_or_404(CandidateMaster,pk=pk)
        serializer = CandidateSerializer(candidate)
        return Response({'serializer':serializer, 'candidate':candidate})



    def put(self,request,pk):
        candidate = get_object_or_404(CandidateMaster, pk=pk)
        serializer = CandidateSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('candidate_list')

        return Response({'serializer':serializer, 'candidate':candidate})






