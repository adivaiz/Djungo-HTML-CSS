from django.shortcuts import render,get_object_or_404
from .models import post



def starting_page(request):
    latest_posts=post.objects.all().order_by("-date")[:3] #get all post sorted new to old and show the 3 in the opening
    return render(request,"blog/index.html",{"posts":latest_posts})

def posts(request):
    all_posts=post.objects.all().order_by("-date")
    return render(request,"blog/allposts.html",{
        "all_posts":all_posts
    })


def post_details(request, slug):
    identified_post=get_object_or_404(post,slug=slug)
    return render(request, 'blog/post-details.html',{
        "post":identified_post,
        "post_tags":identified_post.tags.all()
    })