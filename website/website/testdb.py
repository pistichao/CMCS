from django.http import HttpResponse

from TestModel.models import Test


# database operations
def testdb(request):
    test1 = Test(name='chris')
    test1.save()
    return HttpResponse("<p>Data Added!</p>")


# get all
def get(request):
    response1 = ""

    data = Test.objects.all()

    for var in data:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


# update
def u(request):
    test1 = Test.objects.get(id=1)
    test1.name = 'eaves'
    test1.save()
    return HttpResponse("<p>Modified!</p>")


# delete
def d(request):
    test1 = Test.objects.get(id=1)
    test1.delete()

    return HttpResponse("<p>Deleted!</p>")
