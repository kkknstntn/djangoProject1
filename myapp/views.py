from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.urls import path
from django.db import transaction
from django.shortcuts import render
from django.db import connection
from myapp.models import displaydata
from myapp.models import Faculties
def tablesjoin(request):
    cursor = connection.cursor()
    cursor.execute(f"Select * from scores_2()")
    results=cursor.fetchall()
    return render(request, 'Index.html', {'displaydata': results})
# Create your views here.
