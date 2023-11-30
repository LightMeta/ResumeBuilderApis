from django.db import models
from .choices import TECH_SKILLS

class Candidate(models.Model):
    ''' 
        This model is regarding the information about the candidate.
        We have saved the techskills in Django's EnumField.    
    '''

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=500, blank = True, null = True)
    number = models.CharField(max_length=15)
    email = models.EmailField(max_length = 254)
    location = models.CharField(max_length=50)
    experience = models.CharField(max_length=1000)
    TECH_SKILLS = models.CharField(max_length=30,blank=True,null=True)

class MultiCandidates(models.Model):
    '''
        This model will have single, that field that will insert all recods together in Candidatemodel.
    '''
    multi_candidates = models.TextField()
