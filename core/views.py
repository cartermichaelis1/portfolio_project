from django.shortcuts import render, get_object_or_404
from .models import Project, Skill
from .forms import ContactForm


def home(request):
    featured_projects = Project.objects.filter(is_featured=True)
    return render(request, 'home.html', {'featured_projects': featured_projects})


def about(request):
    return render(request, 'about.html')


def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': all_projects})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    tools = [t.strip() for t in project.tools_used.split(',')]
    return render(request, 'project_detail.html', {'project': project, 'tools': tools})


def skills(request):
    category_order = ['programming', 'ai_tools', 'marketing', 'analytics', 'other_tools']
    groups = []
    for cat in category_order:
        qs = Skill.objects.filter(category=cat).order_by('-proficiency')
        if qs.exists():
            groups.append({'label': qs.first().get_category_display(), 'skills': qs})
    return render(request, 'skills.html', {'groups': groups})


def resume(request):
    return render(request, 'resume.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_500(request):
    return render(request, '500.html', status=500)
