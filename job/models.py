import email
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.


JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Work From Home', 'Work From Home'),
    ('Shift Based', 'Shift Based'),
)

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

class Job(models.Model): #table
    owner = models.ForeignKey( User , related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100) #column
    # loction
    job_type = models.CharField(max_length=15, choices=JOB_TYPE, default="Full Time")
    description = models.TextField(max_length=2000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default='IT/Software Development') #1 to many realtion, #on_delete=models.CASCADE if daelted categry will delete every thing with it cheak docmtion
    image = models.ImageField(upload_to=image_upload)

    slug = models.SlugField(blank=True, null=True)
    # - Experience
    # - Gender

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)# remove slug fy from title and m
        super(Job, self).save(*args, **kwargs)



    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE )
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name