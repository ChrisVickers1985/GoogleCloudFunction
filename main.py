import functions_framework

@functions_framework.http
def hello_http(request):
    return 'Hello Github! I just updated this.'
