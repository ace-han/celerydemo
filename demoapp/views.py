from django.http.response import HttpResponse

from demoapp.tasks import mul, xsum


def index(request):
    x = request.GET.get('x', 4)
    y = request.GET.get('y', 8)
    mul_result = mul.delay(x, y)  # @UndefinedVariable
    xsum_result = xsum.delay([x, y]) # @UndefinedVariable
    result_tpl = 'task scheduled, mul: %s, xsum: %s ' % (mul_result, xsum_result)
    return HttpResponse( result_tpl )