from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from apiv0t3.models import (Candidate, Elector, Vote)
from apiv0t3.api.serializers import (CandidateSerializer, 
									 ElectorSerializer, 
									 VoteSerializer)

class ElectorListCreateAPIView(APIView):
	
	def get(self, request):
		electors = Elector.objects.all()
		serializer = ElectorSerializer(electors, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ElectorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ElectorDetailCreateAPIView(APIView):

	def get_object(self, pk):
		elector = get_object_or_404(Elector, pk=pk)
		return elector

	def get(self, request, pk):
		elector = self.get_object(pk)
		serializer = ElectorSerializer(elector)
		return Response(serializer.data)

	def put(self, request, pk):
		elector = self.get_object(pk)
		serializer = ElectorSerializer(elector, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		elector = self.get_object(pk)
		elector.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class VoteListCreateAPIView(APIView):
	
	def get(self, request):
		vote = Vote.objects.all()
		serializer = VoteSerializer(vote, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = VoteSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VoteDetailCreateAPIView(APIView):

	def get_object(self, pk):
		vote = get_object_or_404(Vote, pk=pk)
		return vote

	def get(self, request, pk):
		vote = self.get_object(pk)
		serializer = VoteSerializer(vote)
		return Response(serializer.data)

	def put(self, request, pk):
		vote = self.get_object(pk)
		serializer = VoteSerializer(vote, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		vote = self.get_object(pk)
		vote.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)