import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='brandcaptcha',
    version='0.1',
    packages=find_packages(),
    package_data={'': ['templates/*.html']},
    include_package_data=True,
    license='MIT License',
    description='BrandCaptcha Django app.',
    long_description=README,
    url='http://github.com/filmow',
    author='Filmow',
    author_email='devs@filmow.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
