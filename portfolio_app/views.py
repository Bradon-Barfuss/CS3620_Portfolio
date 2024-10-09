from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .models import Contact
from .forms import ContactForm
from django.template import loader
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    """A view for the portofilo home page

    Args:
        request: The http request object

    Returns:
        rendered http object using templates displaying infomation about bradon.
    """
    item_list = """Hi! <br> My Name is bradon barfuss! I am a highly motivated Computer Scientist specializing in software development and machine learning. 
    Experience in full-stack development, UI/UX design, Object-Oriented Programming, and cloud-based 
    development. Strong background in collaborative team environments, coding, testing, and deployment 
    across various platforms using SDLC. """
    context = {'item_list': item_list, }
    return render(request, 'portfolio_app/index.html', context)


def Project(request):
    """ Display Project Items

    Args:
        request: The http request object

    Returns:
        rendered http object using templates displaying infomation about bradon coding projects.
    """
    item_list = Project.objects.all()
    context = {'item_list': item_list, }
    return render(request, 'portfolio_app/Project.html', context)

@login_required
def contact(request):
    """Return Contact Email

    Args:
        request: Http request object

    Returns:
        Http response of Bradons email.
    """
    contact_item = Contact.objects.all()
    context = {'contact_item': contact_item, }


    return render(request, 'portfolio_app/contact.html', context)


def projectShowcase(request, portfolio_id):
    """Show case a single project from portfolio

    Args:
        request: Http request object
        portfolio_id: The ID (Primary Key) of the displayed portfolio project

    Returns:
        A http request using render, using a template to only display one portfolio project
    """
    project_item = Portfolio.objects.get(pk=portfolio_id)
    project_highlights = project_item.project_highlights.split('\n')
    project_features = project_item.features.split('\n')
    project_implementations = project_item.implementation_details.split('\n')

    context = {'project_item': project_item,
               'project_highlights': project_highlights, 
               'project_features': project_features,
               'project_implementations': project_implementations,

               }
    return render(request, 'portfolio_app/projectShowcase.html', context)






def create_contact(request):
    form = ContactForm(request.POST or None)

    if(form.is_valid()):
        form.save()
        return redirect('../')
    
    return render(request, 'portfolio_app/contact-form.html', {'form': form})



def update_contact(request, contact_id):
    contact_item = Contact.objects.get(id=contact_id)

    form = ContactForm(request.POST or None, instance=contact_item)

    if form.is_valid():
        form.save()
        return redirect('../')
    
    return render(request, 'portfolio_app/contact-form.html', {'form': form, 'contact_item': contact_item})



def delete_contact(request, contact_id):
    contact_item = Contact.objects.get(id=contact_id)
    contact_item.delete()
    return redirect('../contact')
