import datetime

from django.db import models
from django.utils.functional import cached_property

class User(models.Model):
    '''
    User Information Model
    '''
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    nickname = models.CharField(max_length=32, unique=True, null=False)
    phone = models.CharField(max_length=16, unique=True, null=False)

    gender = models.CharField(max_length=8,choices=GENDER)
    birth_year = models.IntegerField(default=2000)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=32) # user location

    @cached_property
    def age(self):
        today = datetime.date.today()
        birth_date = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        times = today - birth_date
        return times.days // 365

    @property
    def profile(self):
        '''
        One to One relationship
        '''
        if not hasattr(self, '_profile'): # check if the profile has init
            _profile, created = Profile.objects.get_or_create(id=self.id)
            self._profile = _profile
        return self._profile

class Profile(models.Model):
    '''
    User Setting Profile
    '''
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    dating_gender = models.CharField(default='Male',max_length=8, choices=GENDER, verbose_name='dating gender')

    location =models.CharField(max_length=32, verbose_name="accepted city")

    min_distance = models.IntegerField(default=1, verbose_name='min distance')
    max_distance = models.IntegerField(default=10, verbose_name='max distance')

    min_dating_age = models.IntegerField(default=18, verbose_name='min age of dating')
    max_dating_age = models.IntegerField(default=45, verbose_name='max age of dating')

    vibration = models.BooleanField(default=True, verbose_name='open vibe')
    only_match = models.BooleanField(default=True, verbose_name='allowed check only matched')
    auto_play = models.BooleanField(default=True, verbose_name='awak on play')

