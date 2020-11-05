from django.db import models


class ProgrammingLanguage(models.Model):
    #project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    project_name = models.CharField(max_length=500)
    date_start = models.DateField('Start date')
    date_end = models.DateField('End date')
    duration = models.IntegerField('Duration (months)', default=0) # in months
    description = models.CharField(max_length=5000)
    website_link = models.CharField(max_length=500)
    location_city = models.CharField('City', max_length=200, default='')
    location_country = models.CharField('Country', max_length=200, default='')
    languages = models.ManyToManyField(
        ProgrammingLanguage,
        through='LanguageToProject',
        through_fields=('project', 'language'),
    )

    def __str__(self):
        return self.project_name


class LanguageToProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE)



class Teammate(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    contact_link = models.CharField(max_length=500)

    def __str__(self):
        return self.last_name
