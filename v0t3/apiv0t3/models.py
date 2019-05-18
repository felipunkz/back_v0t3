from django.db import models

# Modelo para Elector

class Elector(models.Model):
	name = models.CharField(max_length=50)
	lastname1 = models.CharField(max_length=50)
	lastname2 = models.CharField(max_length=50)
	street = models.CharField(max_length=100)
	street_number = models.CharField(max_length=20)
	neighbourhood = models.CharField(max_length=50)
	county = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	sex = models.CharField(max_length=1)
	age = models.SmallIntegerField()
	voted = models.BooleanField(default=False)

	def _get_full_name(self):
		"Returns the elector's full name"
		return '%s %s %s' % (self.name, self.lastname1, self.lastname2)
	full_name = property(_get_full_name)

	class Meta:
		ordering = ['name', 'lastname1', 'lastname2']

# Modelo para Candidato

class Candidate(models.Model):
	name = models.CharField(max_length=50)
	lastname1 = models.CharField(max_length=50)
	lastname2 = models.CharField(max_length=50)
	party = models.CharField(max_length=60)
	office = models.CharField(max_length=60)

	def _get_full_name(self):
		"Returns the candidate's full name"
		return '%s %s %s' % (self.name, self.lastname1, self.lastname2)
	full_name = property(_get_full_name)

	class Meta:
		ordering = ['name', 'lastname1', 'lastname2']

# Modelo para Voto

class Vote(models.Model):
	name_candidate = models.CharField(max_length=50)
	lastname1_candidatename_candidate = models.CharField(max_length=50)
	lastname2_candidatename_candidate = models.CharField(max_length=50)
	county = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	sex = models.CharField(max_length=1)
	age = models.SmallIntegerField()
	date_emitted = models.DateTimeField(auto_now_add=True)