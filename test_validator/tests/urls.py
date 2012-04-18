from django.conf.urls import patterns
from django.http import HttpResponse

VALID_HTML = """
<!DOCTYPE html>
<html>
<head><title>title</title></head>
<body>valid</body>
</html>
"""
INVALID_HTML = VALID_HTML.replace('/', '')

urlpatterns = patterns('',
    (r'^valid/$', lambda r: HttpResponse(VALID_HTML)),
    (r'^invalid/$', lambda r: HttpResponse(INVALID_HTML)),
)
