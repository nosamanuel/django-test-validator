import sys

from django.conf import settings

settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
            },
        },
    INSTALLED_APPS=('test_validator',),
    ROOT_URLCONF='test_validator.tests.urls',
    )

from django.test.utils import get_runner


def run_tests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['test_validator'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    run_tests()
