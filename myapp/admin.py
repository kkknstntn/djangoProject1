from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html

from django.urls import path

from .models import Universities
from .models import Faculties
from .models import Chairs
from .models import Lecturers
from .models import Disciplines
from .models import ChairLecturer
from .models import Spec
from .models import Orders
from .models import Marks
from .models import Studentgroups
from .models import Students
from .models import universities_view
from .models import lecturers_view
from .models import univ_fac

class FacultiesInline(admin.TabularInline):
    model = Faculties
class ChairsInline(admin.TabularInline):
    model = Chairs

class StunetsInline(admin.TabularInline):
    model = Students

class MarksInline(admin.TabularInline):
    model = Marks

from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import admin
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect

from myapp.views import tablesjoin
class UniversitiesAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ('firstname', 'creationdate', 'address')


    inlines = [FacultiesInline]

class FacultiesAdmin(admin.ModelAdmin):
    list_display = ('facname', 'phone', 'address')


    inlines = [ChairsInline]

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'groupid')
    change_form_template = "temp2.html"
    def response_change(self, request, obj):
        if "_make" in request.POST:
            self.message_user(request, "ok")
            return tablesjoin(request)
        return super().response_change(request, obj)


    inlines = [MarksInline]

class StudentgroupsAdmin(admin.ModelAdmin):
    list_display = ('course','groupnumber')
    inlines = [StunetsInline]

class Univ_facAdmin(admin.ModelAdmin):
    list_display = ('id','universityid', 'facname', "firstname")
    search_fields = ( "firstname",'facname')
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


class LecturersAdmin( admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'middlename', 'post')





admin.site.register(Chairs)
admin.site.register(Universities, UniversitiesAdmin)
admin.site.register(Faculties,FacultiesAdmin)
admin.site.register(univ_fac,Univ_facAdmin)
admin.site.register(Lecturers,LecturersAdmin)
admin.site.register(Disciplines)
admin.site.register(Spec)
admin.site.register(Orders)
admin.site.register(ChairLecturer)

admin.site.register(Students,StudentsAdmin)
admin.site.register(Studentgroups,StudentgroupsAdmin)
admin.site.register(Marks)
