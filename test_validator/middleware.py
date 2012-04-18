from tidylib import tidy_document


class HTMLValidationError(Exception):
    pass


class HTMLValidationMiddleware(object):
    def process_response(self, request, response):
        if 'text/html' in response['Content-Type'] and response.content:
            document, errors = tidy_document(response.content)
            if errors:
                raise HTMLValidationError(errors)

        return response
