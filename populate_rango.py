import django
import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

django.setup()
from rango.models import Category, Page


def populate():
    python_pages = [{'title': 'Official Python Tutorial',
                     'url': 'http://docs.python.org/3/tutorial/'},
                    {'title': 'How to Think like a Computer Scientist',
                     'url': 'http://www.greenteapress.com/thinkpython/'},
                    {'title': 'Learn Python in 10 Minutes',
                     'url': 'http://www.korokithakis.net/tutorials/python/'}]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/'},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/'}]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/'},

        {'title': 'Flask',
         'url': 'http://flask.pocoo.org'}]

    cats = {'Python': {'pages': python_pages},
            'Django': {'pages': django_pages},
            'Other Frameworks': {'pages': other_pages}}

    def add_cat(name):
        if name == 'Python':
            views, likes = 128, 64
        elif name == 'Django':
            views, likes = 64, 32
        else:
            views, likes = 32, 16

        c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
        c.save()
        return c

    def add_page(cat, title, url, views=0):
        views = random.randint(2, 30)
        p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
        p.save()
        return p

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p} ')


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
