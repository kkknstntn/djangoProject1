# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse



class Universities(models.Model):
    list_display = ('firstname', 'creationdate', 'address')
    firstname = models.CharField(max_length=30, blank=True, null=True)
    creationdate = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'universities'


class displaydata(models.Model):
    list_display = ('facname', 'phone', 'address')
    universityid = models.ForeignKey('Universities', models.DO_NOTHING, db_column='universityid')
    facname = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
class Faculties(models.Model):
    universityid = models.ForeignKey('Universities', models.DO_NOTHING, db_column='universityid')
    facname = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faculties'

class Chairs(models.Model):
    facultyid = models.ForeignKey('Faculties', models.DO_NOTHING, db_column='facultyid')
    chairname = models.CharField(max_length=100, blank=True, null=True)
    all_books = Faculties.objects.all()
    class Meta:
        managed = False
        db_table = 'chairs'


class Lecturers(models.Model):
    chairid = models.ForeignKey(Chairs, models.DO_NOTHING, db_column='chairid', blank=True, null=True)
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    middlename = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    academicdegreename = models.CharField(max_length=30, blank=True, null=True)
    post = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lecturers'


class ChairLecturer(models.Model):
    chairid = models.ForeignKey('Chairs', models.DO_NOTHING, db_column='chairid', blank=True, null=True)
    lecturerid = models.ForeignKey('Lecturers', models.DO_NOTHING, db_column='lecturerid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chair_lecturer'


class Disciplines(models.Model):
    hours = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    disciplinename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplines'


class LecturersDisciplines(models.Model):
    disciplineid = models.ForeignKey(Disciplines, models.DO_NOTHING, db_column='disciplineid')
    groupid = models.ForeignKey('Studentgroups', models.DO_NOTHING, db_column='groupid')
    lecturerid = models.ForeignKey(Lecturers, models.DO_NOTHING, db_column='lecturerid')

    class Meta:
        managed = False
        db_table = 'lecturers_disciplines'


class Marks(models.Model):
    studentid = models.ForeignKey('Students', models.DO_NOTHING, db_column='studentid')
    typeofcontrl = models.CharField(max_length=30, blank=True, null=True)
    dicsiplineid = models.ForeignKey(Disciplines, models.DO_NOTHING, db_column='dicsiplineid')
    scores = models.IntegerField(blank=True, null=True)
    mark = models.IntegerField()
    numberofpasses = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'marks'


class Orders(models.Model):
    studentid = models.ForeignKey('Students', models.DO_NOTHING, db_column='studentid')
    doing = models.CharField(max_length=30, blank=True, null=True)
    ordername = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Spec(models.Model):
    chairid = models.ForeignKey(Chairs, models.DO_NOTHING, db_column='chairid')
    specname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spec'


class Studentgroups(models.Model):
    course = models.SmallIntegerField(blank=True, null=True)
    groupnumber = models.SmallIntegerField()
    chairid = models.ForeignKey(Chairs, models.DO_NOTHING, db_column='chairid', blank=True, null=True)
    specid = models.ForeignKey(Spec, models.DO_NOTHING, db_column='specid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'studentgroups'


class Students(models.Model):
    groupid = models.ForeignKey(Studentgroups, models.DO_NOTHING, db_column='groupid')
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    middlename = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    lang = models.CharField(max_length=30, blank=True, null=True)
    birthdate = models.DateField()
    post = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'

class universities_view(models.Model):
    list_display = ('firstname', 'creationdate', 'address')
    firstname = models.CharField(max_length=30, blank=True, null=True)
    creationdate = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'universities'

class lecturers_view(models.Model):
    chairid = models.ForeignKey(Chairs, models.DO_NOTHING, db_column='chairid', blank=True, null=True)
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    middlename = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    academicdegreename = models.CharField(max_length=30, blank=True, null=True)
    post = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lecturers'

class univ_fac(models.Model):
    universityid = models.ForeignKey('Universities', models.DO_NOTHING, db_column='universityid')
    facname = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'univ_fac'
