# Django Test Validator

A Django app for validating HTML during testing. Any views run by your test suite that return invalid HTML will raise an `HTMLValidationError`.

## Usage

Add `test_validator` to your installed apps. Then, instead of this...

    python manage.py test ...

...run this:

    python manage.py test_validate ...

## License

MIT
