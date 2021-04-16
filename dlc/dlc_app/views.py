from django.shortcuts import render, get_object_or_404
from .models import Comment, Recept
from .forms import CommentForm


def index(request):
    recepts = Recept.objects.all().order_by("-created_at")[:7]
    the_best = Recept.objects.all().order_by("-stars")[:6]
    small_comments = []
    small = Recept.objects.all().order_by("-created_at")[:9]
    for s in small:
        small_comments.append(len(Comment.objects.filter(recept_id=s.id)))

    ctx = {
        "recepts": recepts,
        "the_best": the_best,
        "small": zip(small, small_comments),
        "stars": [1, 2, 3, 4, 5],
    }
    return render(request, 'index.html', ctx)


def test(request):
    all_elements = Recept.objects.all()
    element_by_id = Recept.objects.get(pk=2)
    element_by_field = Recept.objects.get(pk=2)
    filtered_elements = Recept.objects.all().filter(image='recept')
    ordered_elements = Recept.objects.all().order('created_at')
    return render(request, 'elements.html', {})


def elements(request):
    foods = Recept.objects.all()[:3]
    return render(request, 'elements.html', {"foods": foods})


def contact(request):
    return render(request, 'contact.html', {})


def recupp(request):
    return render(request, 'recept.html', {})


def blogpost(request):
    return render(request, 'blog-post.html', {})


def blog_2(request):
    return render(request, 'blog_2.html', {})


def blog_3(request):
    return render(request, 'blog_3.html', {})


def burger(request):
    return render(request, 'burger.html', {})


def recept(request, recept_id):
    recept = get_object_or_404(Recept, pk=recept_id)
    form = CommentForm(request.POST or None)
    if request.POST:
        print("Form Error:", form.errors)
        if form.is_valid():
            form.save()

    ctx = {
        "recept": recept
    }
    return render(request, 'receipe-post.html', ctx)


def sushi(request):
    return render(request, 'sushi.html', {})


def blog_2(request):
    return render(request, 'blog_2.html', {})


def about(request):
    return render(request, 'about.html', {})


def all(request, all_id):
    recept = get_object_or_404(Recept, pk=all_id)
    return render(request, 'all_recepts.html', {"recept": recept})
