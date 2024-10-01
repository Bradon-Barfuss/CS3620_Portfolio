from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio
from .models import Hobbies
from django.template import loader


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


def hobbies(request):
    """Display All Hobbies

    Args:
        request: The http request object

    Returns:
        rendered http object using templates displaying infomation about bradon hobbies.
    """
    item_list = Hobbies.objects.all()
    context = {'item_list': item_list, }
    return render(request, 'portfolio_app/hobbies.html', context)


def portfolio(request):
    """ Display Portfolio Items

    Args:
        request: The http request object

    Returns:
        rendered http object using templates displaying infomation about bradon coding projects.
    """
    item_list = Portfolio.objects.all()
    context = {'item_list': item_list, }
    return render(request, 'portfolio_app/portfolio.html', context)


def contact(request):
    """Return Contact Email

    Args:
        request: Http request object

    Returns:
        Http response of Bradons email.
    """
    return render(request, 'portfolio_app/contact.html')


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

def hobbyShowcase(request, hobby_id):
    """Show case a single hobby from portfolio

    Args:
        request: Http request object
        hobby_id: The ID (Primary Key) of the displayed portfolio project

    Returns:
        A http request using render, using a template to only display one portfolio hobby
    """

    hobby_item = Hobbies.objects.get(pk=hobby_id)

    context = {'hobby_item': hobby_item,}
    return render(request, 'portfolio_app/hobbyShowcase.html', context)
