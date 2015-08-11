##### Install the first Django app (Object DB Management)

```
$ pip install django
$ python -c "import django; print(django.get_version())"
$ django-admin startproject icecream
$ tree icecream
icecream
├── icecream
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

```

```
$ cd icecream && python manage.py startapp flavors
$ vim icecream/settings.py
    add 'flavors' to INSTALLED_APPS:
$ vim flavors/modeles.py

from django.db import models

# Create your models here.
class Flavors(models.Model):
    name = models.TextField()
    price = models.TextField()
    type = models.TextField()

    def __str__(self):
        return "{} {}".format(self.name, self.price)
```

```
-<%>- python manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: staticfiles, messages
  Apply all migrations: admin, flavors, contenttypes, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying flavors.0001_initial... OK
  Applying sessions.0001_initial... OK
```

```
-<%>- python manage.py shell
Python 2.7.8 (default, Aug  8 2015, 11:56:52)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.56)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from flavors.models import Flavors
>>> flavor = Flavors(name='Vanilla ice cream', price='5.00', type='regular')
>>> flavor.save()
>>> flavor.id
1
>>> str(flavor.name)
'Vanilla ice cream'
>>> str(flavor.price)
'5.00'

>>> flavor = Flavors(name='Stracciatella', price='20.00', type='gelato')
>>> flavor.id
>>> flavor.save()
>>> flavor.id
2
```

```
>>> from flavors.models import Flavors
>>> flavor = Flavors.objects.first()
>>> flavor.name
u'Vanilla ice cream'
>>> flavor = Flavors.objects.get(name='Vanilla ice cream')
>>> flavor.name
u'Vanilla ice cream'
>>> flavor = Flavors.objects.get(name='Stracciatella')
>>> flavor.name
u'Stracciatella'
>>> flavor.id
2
```

```
>>> list(Flavors.objects.values_list('name', flat=True))
[u'Vanilla ice cream', u'Stracciatella']

>>> f = Flavors.objects.order_by('price')
>>> print f
[<Flavors: Stracciatella 20.00>, <Flavors: Vanilla ice cream 5.00>]
```

```
>>> queryset = Flavors.objects.all()
>>> for qs in queryset.iterator():
...    print qs
...
Vanilla ice cream 5.00
Stracciatella 20.00
```

```
>>> from flavors.models import Flavors
>>> queryset = Flavors.objects.all().order_by('price')
>>> for qs in queryset.iterator():
...    print qs
...
Stracciatella 20.00
Vanilla ice cream 5.00
```
