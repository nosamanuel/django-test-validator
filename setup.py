import os
from setuptools import setup


def is_package(path):
    return (
        os.path.isdir(path) and
        os.path.isfile(os.path.join(path, '__init__.py'))
        )


def find_packages(path, base=""):
    packages = {}
    for item in os.listdir(path):
        dir = os.path.join(path, item)
        if is_package(dir):
            if base:
                module_name = "%(base)s.%(item)s" % vars()
            else:
                module_name = item
            packages[module_name] = dir
            packages.update(find_packages(dir, module_name))
    return packages


setup(name='django-test-validator',
      version='0.1',
      url='http://github.com/nosamanuel/django-test-validator/',
      license='MIT',
      description='A Django app for validating HTML during testing',
      long_description='',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Text Processing :: Markup :: HTML'
        ],
      maintainer='Noah Seger',
      packages=find_packages('.').keys(),
      install_requires=['pytidylib'],
      test_suite='test',
      tests_require=['Django', 'pytidylib'],
      )
