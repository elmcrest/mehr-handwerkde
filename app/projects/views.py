import os
import json
import uuid

from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from martor.utils import LazyEncoder
from django.views.generic import ListView
from .models import Project


class ProjectListView(ListView):
    class Meta:
        model = Project


@login_required
def markdown_uploader(request):
    """
    custom image upload for martor markdown editor
    """
    if request.method == "POST" and request.is_ajax():
        if "markdown-image-upload" in request.FILES:
            image = request.FILES["markdown-image-upload"]
            image_types = [
                "image/png",
                "image/jpg",
                "image/jpeg",
                "image/pjpeg",
                "image/gif",
            ]
            if image.content_type not in image_types:
                data = json.dumps(
                    {"status": 405, "error": _("Bad image format.")}, cls=LazyEncoder
                )
                return HttpResponse(data, content_type="application/json", status=405)
            if image.size > settings.MAX_IMAGE_UPLOAD_SIZE:
                to_Mb = settings.MAX_IMAGE_UPLOAD_SIZE / (1024 * 1024)
                data = json.dumps(
                    {"status": 405, "error": _(f"Maximum image file is {to_Mb} MB."),},
                    cls=LazyEncoder,
                )
                return HttpResponse(data, content_type="application/json", status=405)
            img_uuid = f"{uuid.uuid4().hex[:10]}-{image.name.replace(' ', '-')}"
            tmp_file = os.path.join(settings.MARTOR_UPLOAD_PATH, img_uuid)
            def_path = default_storage.save(tmp_file, ContentFile(image.read()))
            img_url = os.path.join(settings.MEDIA_URL, def_path)

            data = json.dumps({"status": 200, "link": img_url, "name": image.name})
            return HttpResponse(data, content_type="application/json")
        return HttpResponse(_("Invalid request!"))
    return HttpResponse(_("Invalid request!"))
