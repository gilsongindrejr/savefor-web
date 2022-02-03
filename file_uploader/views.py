from django.shortcuts import render
from django.views import View
from django.core.exceptions import PermissionDenied

from .models import File
from .forms import FileForm


class UploadView(View):

    def post(self, request):
        if request.user.is_authenticated is not True:
            raise PermissionDenied()
        context = {}
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = File(file=request.FILES['file'])
            new_file.author = request.user
            new_file.save()
            context['message'] = 'File uploaded successfully!'
        form = FileForm()
        context['form'] = form
        return render(request, 'file_uploader/upload.html', context)

    def get(self, request):
        if request.user.is_authenticated is not True:
            raise PermissionDenied()
        form = FileForm()
        context = {'form': form}
        return render(request, 'file_uploader/upload.html', context)
