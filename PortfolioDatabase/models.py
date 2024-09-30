from django.db import models

# Create your models here.

class Portfolio(models.Model):
    def __str__(self):
        return "Project Name: " + self.project_name + " || Project Description: " +  self.project_desc + " || Project Lanaguage: " + self.project_language + "<br>" #When you run Item.objects.all(), you will get the item name becasue of this

    project_name = models.CharField(max_length=255)
    project_desc = models.CharField(max_length=1000)
    project_language = models.CharField(max_length=255)

class Hobbies(models.Model):
    def __str__(self):
        return "Hobby Name: " + self.hobby_name + " || Hobby Description: " +  self.hobby_desc + "<br>"

    hobby_name = models.CharField(max_length=255)
    hobby_desc = models.CharField(max_length=1000)