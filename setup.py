import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-postal",
    version = "0.8",
    url = 'http://github.com/mthornhill/django-postal',
    license = 'BSD',
    description = "A Django app for l10n of postal addresses.",
    long_description = read('README'),

    author = 'Michael Thornhill',
    author_email = 'michael@maithu.com',

    packages = find_packages('src'),
    package_dir = {'': 'src'},
    package_data={'':['*.txt', '*.js', '*.html', '*.*']},

    install_requires = ['setuptools','django-countries','django-piston'],

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
