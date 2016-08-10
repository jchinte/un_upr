from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import title
from cgitb import text
from django.utils.encoding import smart_unicode


# Create your models here.

questions =[
            'Name',
            'Sex',
            'Date of Birth',
            ] 

class OrganizationTypes(models.Model):
    type = models.CharField(max_length=100)
 

class Organization(models.Model):
    name = models.CharField(max_length=100)
    un_name = models.CharField(max_length=100,blank=True)
    acronym = models.CharField(max_length=100)
    type =  models.ForeignKey(OrganizationTypes)

class UserMeta(models.Model):

    pass

class UPR_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Organization = models.ForeignKey(Organization)
    streetAddress = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    meta = models.ForeignKey(UserMeta, blank = True, null=True)
    phone = models.CharField(max_length=100)
    website = models.URLField(blank = True)


class UPR_submission(models.Model):
    
    
    #victim information here
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=101)
    #__questions = []
   
    
    
    def __unicode__(self):
        return smart_unicode(self.title)

    
    
class UPR_question(models.Model):
    question = models.CharField(max_length=200)
    submission = models.ForeignKey(UPR_submission)
    answer = models.TextField(max_length=10000)
    
   
       
    def getQuestion(self):
        if self.pk is int:
            return self.data['questionText']
        return None
    def setQuestion(self, q = "Information:"):
        self.data['questionText'] = q
    
    def __unicode__(self):
        return smart_unicode(self.answer)
    
    
    
class SampleQuestion(UPR_question):
    class Meta:
        proxy=True
    def __init__(self, *args, **kwargs):
        super(SampleQuestion, self).__init__(args, kwargs)
        self.setQuestion("This is a sample question.")
        
        
        
        
"""       
{% for q in questions %}
{{ q.text }}
{{ q.form.answer }}
{% endfor %}

"""

questions = [
             UPR_question("name"),
             UPR_question("sex")
             ]
