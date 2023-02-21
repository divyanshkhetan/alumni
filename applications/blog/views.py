from django.shortcuts import render
from applications.blog.models import Tags

import operator

# Create your views here.
def index(request):


    no_of_tags_for_homepage = 5
    tags = Tags.objects.filter(on_home_page=True).order_by('-last_modified')[:no_of_tags_for_homepage]
    if tags.count() == 0:
        tags = Tags.objects.all().order_by('-last_modified')[:no_of_tags_for_homepage]

    context = {
        'tags': tags,
    }
    return render(request, "blog/home.html", context)
