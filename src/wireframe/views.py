from django.shortcuts import render


def about(request):
    return render(request, 'wireframe/about.html', {})


def project_version(request):
    return render(request, 'wireframe/version.html', {})

