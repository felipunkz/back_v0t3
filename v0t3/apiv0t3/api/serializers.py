from rest_framework import serializers
from apiv0t3.models import Candidate, Elector, Vote

class CandidateSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField()
	lastname1 = serializers.CharField()
	lastname2 = serializers.CharField()
	party = serializers.CharField()
	office = serializers.CharField()

	def create(self, validated_data):
		return Candidate.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.lastname1 = validated_data.get('lastname1', instance.lastname1)
		instance.lastname2 = validated_data.get('lastname2', instance.lastname2)
		instance.party = validated_data.get('party', instance.party)
		instance.office = validated_data.get('office', instance.office)
		instance.save()
		return instance


class ElectorSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField()
	lastname1 = serializers.CharField()
	lastname2 = serializers.CharField()
	street = serializers.CharField()
	street_number = serializers.CharField()
	neighbourhood = serializers.CharField()
	county = serializers.CharField()
	state = serializers.CharField()
	sex = serializers.CharField()
	age = serializers.IntegerField()
	voted = serializers.BooleanField()

	def create(self, validated_data):
		return Elector.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', name)
		instance.lastname1 = validated_data.get('lastname1', lastname1)
		instance.lastname2 = validated_data.get('lastname2', lastname2)
		instance.street = validated_data.get('street', street)
		instance.street_number = validated_data.get('street_number', street_number)
		instance.neighbourhood = validated_data.get('neighbourhood', neighbourhood)
		instance.county = validated_data.get('county', county)
		instance.state = validated_data.get('state', state)
		instance.sex = validated_data.get('sex', sex)
		instance.age = validated_data.get('age', age)
		instance.voted = validated_data.get('voted', voted)
		instance.save()
		return instance

class VoteSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name_candidate = serializers.CharField()
	lastname1_candidatename_candidate = serializers.CharField()
	lastname2_candidatename_candidate = serializers.CharField()
	county = serializers.CharField()
	state = serializers.CharField()
	sex = serializers.CharField()
	age = serializers.IntegerField()
	date_emitted = serializers.DateTimeField()

	def create(self, validated_data):
		return Vote.objects.crete(**validated_data)

	def update(self, instance, validated_data):
		instance.name_candidate = validated_data.get('name_candidate', name_candidate)
		instance.lastname1_candidatename_candidate = validated_data.get('lastname1_candidatename_candidate', lastname1_candidatename_candidate)
		instance.lastname2_candidatename_candidate = validated_data.get('lastname2_candidatename_candidate', lastname2_candidatename_candidate)
		instance.county = validated_data.get('county', county)
		instance.state = validated_data.get('state', state)
		instance.sex = validated_data.get('sex', sex)
		instance.age = validated_data.get('age', age)
		instance.date_emitted = validated_data.get('date_emitted', date_emitted)
		instance.save()
		return instance

