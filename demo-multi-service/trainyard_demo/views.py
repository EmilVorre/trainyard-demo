import socket

from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

from .models import DeploymentInfo


def index(request):
    hostname = socket.gethostname()

    db_version = None
    db_error = None
    deployment_info = None

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT version()")
            row = cursor.fetchone()
            db_version = row[0].split(",")[0] if row else "unknown"
        deployment_info = DeploymentInfo.objects.first()
    except Exception as e:
        db_error = str(e)

    context = {
        "hostname": hostname,
        "db_version": db_version,
        "db_error": db_error,
        "deployment_info": deployment_info,
    }
    return render(request, "index.html", context)


def health(request):
    return HttpResponse("ok")