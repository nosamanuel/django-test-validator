from django.test import TestCase
from django.test.utils import override_settings

from test_validator.middleware import HTMLValidationError
from test_validator.middleware import HTMLValidationMiddleware

MIDDLEWARE_CLASSES = ('test_validator.middleware.HTMLValidationMiddleware',)


class TestValidator(TestCase):
    def test_views(self):
        response = self.client.get('/valid/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/invalid/')
        self.assertEqual(response.status_code, 200)

    def test_middleware_passes_on_valid_html(self):
        middleware = HTMLValidationMiddleware()
        response = self.client.get('/valid/')
        middleware_response = middleware.process_response(
            response.request, response)
        self.assertEqual(response, middleware_response)

    def test_middleware_raises_on_invalid_html(self):
        middleware = HTMLValidationMiddleware()
        response = self.client.get('/invalid/')
        self.assertRaises(HTMLValidationError, middleware.process_response,
                          response.request, response)

    @override_settings(MIDDLEWARE_CLASSES=MIDDLEWARE_CLASSES)
    def test_middleware_setting_affects_test_client(self):
        self.assertEqual(self.client.get('/valid/').status_code, 200)
        self.assertRaises(HTMLValidationError, self.client.get, '/invalid/')

    def test_management_command(self):
        pass
