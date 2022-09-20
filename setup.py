"""
Install project requirements.
"""

from setuptools import setup, find_packages

setup(
    name="yoyo",
    version="1.0.0",
    description="YOYO API",
    packages=find_packages(),
    include_package_data=True,
    scripts=["manage.py"],
    install_requires=[
        "wheel==0.37.1",
        "Django==4.1.0",
        "djangorestframework==3.13.1",
        "python-decouple==3.6",
        "psycopg2-binary==2.9.3",
        "django-cors-middleware==1.5.0",
        "django-cors-headers==3.10.1",
        "python-dateutil==2.8.2",
        "whitenoise==5.3.0",
        "drf-yasg==1.20.0",
        "dj-database-url==0.5.0",
        "django-rest-swagger==2.2.0",
        "drf-spectacular==0.21.0"
    ],
)
