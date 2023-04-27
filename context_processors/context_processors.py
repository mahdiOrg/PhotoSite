from contact.models import ContactWay


def about_data_c(request):
    aboutData = ContactWay.objects.first()

    return {'about_data': aboutData}
