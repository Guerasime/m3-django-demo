from setuptools import setup, find_packages

setup(
    name="m3-django-demo",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'Django==2.2.28',
        'm3-django-compat==1.9.2',
        'm3-objectpack==2.2.47',
    ],
    dependency_links=[
        'http://pypi.bars-open.ru/simple/'
    ],
    author="Gerasim",
    author_email="nikolaevguerasime@gmail.com",
    description="Django project with M3 and Objectpack",
    url="https://example.com",
)