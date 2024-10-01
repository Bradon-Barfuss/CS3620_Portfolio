from django.db import models

# Create your models here.

class Portfolio(models.Model):
    def __str__(self):
        return "Project Name: " + self.project_name + " || Project Description: " +  self.project_desc + " || Project Lanaguage: " + self.project_language + "<br>" #When you run Item.objects.all(), you will get the item name becasue of this
    
    project_name = models.CharField(max_length=255)
    project_desc = models.CharField(max_length=500)
    project_language = models.CharField(max_length=255)
    project_image = models.CharField(max_length=500, default="https://raw.githubusercontent.com/Bradon-Barfuss/C-Sharp-Programs/main/Invoice%20System/InvoiceMainMenuPicture.png")
    
    github_link = models.URLField(max_length=500, blank=True, null=True)
    project_highlights = models.TextField(blank=True, null=True)
    features = models.TextField(blank=True, null=True) 
    implementation_details = models.TextField(blank=True, null=True) 
    

class Hobbies(models.Model):
    def __str__(self):
        return "Hobby Name: " + self.hobby_name + " || Hobby Description: " +  self.hobby_desc + "<br>"

    hobby_name = models.CharField(max_length=255)
    hobby_desc = models.CharField(max_length=1000)
    hobby_image = models.CharField(max_length=500, default="https://raw.githubusercontent.com/Bradon-Barfuss/C-Sharp-Programs/main/Invoice%20System/InvoiceMainMenuPicture.png")
