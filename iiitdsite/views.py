from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import FacultyPageInfo, NewsLetterEmail, Events, images, About, AboutUsTestimonial
from .models import OurFamilyLink, AcademicsECE, AcademicsCSE, Academics, ResearchPoints, ResearchStudents
from .models import CurriculumLink, NewsPage, AcademicCalLink, HomePageUpcomingEvents, SenateChairperson, SenateMembers, Administration, BOGChairperson, BOGNonMembers, BOGMembers, Staff, FinanceCommitteeMembers
from .models import ugcselinks, phdlinks, Scholarship, Alert, Placements, HomePageGallery, Jobs
from .weather import temp_cel, temp_fah
UserModel = get_user_model()

def home(request):
    alert = Alert.objects.last()
    links = ugcselinks.objects.last()
    events = Events.objects.all()[:3:-1]
    main_event = Events.objects.last()
    upcoming_events = HomePageUpcomingEvents.objects.all()[::-1]
    acad_link = AcademicCalLink.objects.get(id=1)
    main_news = NewsPage.objects.last()
    news = NewsPage.objects.all()[:4:-1]
    currilink = CurriculumLink.objects.get(id=1)
    gallery = HomePageGallery.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('')
    return render(request, 'iiitdsite/index.html', {'alert': alert, 'main_event': main_event, 'events': events, 'gallery': gallery, 'images': images, 'upcoming_events': upcoming_events, 'main_news': main_news, 'acad_link': acad_link, 'news': news, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def homehindi(request):
    alert = Alert.objects.last()
    links = ugcselinks.objects.last()
    events = Events.objects.all()[:3:-1]
    main_event = Events.objects.last()
    upcoming_events = HomePageUpcomingEvents.objects.all()[::-1]
    acad_link = AcademicCalLink.objects.get(id=1)
    main_news = NewsPage.objects.last()
    news = NewsPage.objects.all()[:4:-1]
    currilink = CurriculumLink.objects.get(id=1)
    event = Events.objects.last()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/hindi')
    return render(request, 'iiitdsite/index(hindi).html', {'alert': alert, 'main_event': main_event, 'events': events, 'event': event, 'images': images, 'upcoming_events': upcoming_events, 'main_news': main_news, 'acad_link': acad_link, 'news': news, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})

def homekannada(request):
    alert = Alert.objects.last()
    links = ugcselinks.objects.last()
    events = Events.objects.all()[:3:-1]
    main_event = Events.objects.last()
    upcoming_events = HomePageUpcomingEvents.objects.all()[::-1]
    acad_link = AcademicCalLink.objects.get(id=1)
    main_news = NewsPage.objects.last()
    news = NewsPage.objects.all()[:4:-1]
    currilink = CurriculumLink.objects.get(id=1)
    event = Events.objects.last()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/kannada')
    return render(request, 'iiitdsite/index(kannada).html', {'alert': alert, 'main_event': main_event, 'events': events, 'event': event, 'images': images, 'upcoming_events': upcoming_events, 'main_news': main_news, 'acad_link': acad_link, 'news': news, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})

def faculty(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    facultydatabase = FacultyPageInfo.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/faculty')
    return render(request, 'iiitdsite/faculty.html', {'acad_link': acad_link, 'currilink': currilink,'facultydatabase': facultydatabase, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def facultyhindi(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    facultydatabase = FacultyPageInfo.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/faculty-hindi')
    return render(request, 'iiitdsite/faculty.html',
                  {'acad_link': acad_link, 'currilink': currilink,'facultydatabase': facultydatabase, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def facultykannada(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    facultydatabase = FacultyPageInfo.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/faculty-kannada')
    return render(request, 'iiitdsite/faculty.html',
                  {'acad_link': acad_link, 'currilink': currilink,'facultydatabase': facultydatabase, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def events(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    eventsinfo = Events.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/events')
    return render(request, 'iiitdsite/events.html',
                  {'acad_link': acad_link, 'currilink': currilink,'eventsinfo': eventsinfo, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def eventshindi(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    eventsinfo = Events.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/events-hindi')
    return render(request, 'iiitdsite/events(hindi).html',
                  {'acad_link': acad_link, 'currilink': currilink,'eventsinfo': eventsinfo, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def eventskannada(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    eventsinfo = Events.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/events-kannada')
    return render(request, 'iiitdsite/events(kannada).html',
                  {'acad_link': acad_link, 'currilink': currilink,'eventsinfo': eventsinfo, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def aboutus(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    about = About.objects.all()
    ourfam = OurFamilyLink.objects.all()
    testi = AboutUsTestimonial.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/about')
    return render(request, 'iiitdsite/about_us.html', {'acad_link': acad_link, 'currilink': currilink,'about': about, 'ourfam': ourfam,
                                                       'testi': testi,'temp_cel': temp_cel,
                                                       'temp_fah': temp_fah, 'links': links,})


def aboutushindi(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    about = About.objects.all()
    ourfam = OurFamilyLink.objects.all()
    testi = AboutUsTestimonial.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/about-hindi')
    return render(request, 'iiitdsite/about_us(hindi).html', {'acad_link': acad_link, 'currilink': currilink,'about': about, 'ourfam': ourfam,
                                                       'testi': testi, 'temp_cel': temp_cel,
                                                       'temp_fah': temp_fah, 'links': links,})


def aboutuskannada(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    about = About.objects.all()
    ourfam = OurFamilyLink.objects.all()
    testi = AboutUsTestimonial.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/about-kannada')
    return render(request, 'iiitdsite/about_us(kannada).html', {'acad_link': acad_link, 'currilink': currilink,'about': about, 'ourfam': ourfam,
                                                       'testi': testi, 'temp_cel': temp_cel,
                                                       'temp_fah': temp_fah, 'links': links,})


def academicscse(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    acadcse = AcademicsCSE.objects.all()
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/academics-cse')
    return render(request, 'iiitdsite/acad_cse.html', {'acad_link': acad_link, 'currilink': currilink,'acadcse': acadcse, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def academicscsehindi(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    acadcse = AcademicsCSE.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/academics-cse-hindi')
    return render(request, 'iiitdsite/acad_cse(hindi).html', {'acad_link': acad_link, 'currilink': currilink,'acadcse': acadcse, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def academicscsekannada(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    acadcse = AcademicsCSE.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/academics-cse-kannada')
    return render(request, 'iiitdsite/acad_cse(kannada).html', {'acad_link': acad_link, 'currilink': currilink,'acadcse': acadcse, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def academicsece(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    acadece = AcademicsECE.objects.all()
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/academics-ece')
    return render(request, 'iiitdsite/acad_ece.html', {'acad_link': acad_link, 'currilink': currilink,'acadece': acadece, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def academicsecehindi(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    acadece = AcademicsECE.objects.all()
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/academics-ece-hindi')
    return render(request, 'iiitdsite/acad_ece(hindi).html', {'acad_link': acad_link, 'currilink': currilink,'acadece': acadece, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def academicsecekannada(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    acadece = AcademicsECE.objects.all()
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/academics-ece-kannada')
    return render(request, 'iiitdsite/acad_ece(kannada).html', {'acad_link': acad_link, 'currilink': currilink,'acadece': acadece, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def academics(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    academics = Academics.objects.all()
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/academics')
    return render(request, 'iiitdsite/academics.html', {'acad_link': acad_link, 'currilink': currilink,'academics': academics, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def academicshindi(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    academics = Academics.objects.all()
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/academics-hindi')
    return render(request, 'iiitdsite/academics(hindi).html', {'acad_link': acad_link, 'currilink': currilink,'academics': academics, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def academicskannada(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    academics = Academics.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/academics-kannada')
    return render(request, 'iiitdsite/academics(kannada).html', {'acad_link': acad_link, 'currilink': currilink,'academics': academics, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def contact(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/contact')
    return render(request, 'iiitdsite/contact.html', {'acad_link': acad_link, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def contacthindi(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/contact-hindi')
    return render(request, 'iiitdsite/contact(hindi).html', {'acad_link': acad_link, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def contactkannada(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/contact-kannada')
    return render(request, 'iiitdsite/contact(kannada).html', {'acad_link': acad_link, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def gallery(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/gallery')
    list = Events.objects.order_by('date')[::-1]
    return render(request, 'iiitdsite/gallery.html', {'acad_link': acad_link, 'currilink': currilink, 'list': list, 'images': images, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def galleryhindi(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/gallery-hindi')
    list = Events.objects.order_by('date')[::-1]
    return render(request, 'iiitdsite/gallery(hindi).html', {'acad_link': acad_link, 'currilink': currilink,'list': list, 'images': images, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def gallerykannada(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/gallery-kannada')
    list = Events.objects.order_by('date')[::-1]
    return render(request, 'iiitdsite/gallery(kannada).html', {'acad_link': acad_link, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links, 'list': list, 'images': images})


def jobs(request):
    job_links = Jobs.objects.last()
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/jobs')
    return render(request, 'iiitdsite/jobs.html', {'job_links': job_links, 'acad_link': acad_link, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def jobshindi(request):
    job_links = Jobs.objects.last()
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/jpbs-hindi')
    return render(request, 'iiitdsite/jobs(hindi).html', {'job_links': job_links, 'acad_link': acad_link, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def jobskannada(request):
    job_links = Jobs.objects.last()
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/jobs-kannada')
    return render(request, 'iiitdsite/jobs(kannada).html', {'job_links': job_links, 'acad_link': acad_link, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def newstack(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    num = NewsPage.objects.count()
    main_news = NewsPage.objects.last()
    news = NewsPage.objects.all()[:num-1:-1]
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/newstack')
    return render(request, 'iiitdsite/newstack.html', {'acad_link': acad_link, 'main_news': main_news, 'news': news, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def newstackhindi(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    num = NewsPage.objects.count()
    main_news = NewsPage.objects.last()
    news = NewsPage.objects.all()[:num-1:-1]
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/newstack-hindi')
    return render(request, 'iiitdsite/newstack(hindi).html', {'acad_link': acad_link, 'main_news': main_news, 'news': news, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def newstackkannada(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    num = NewsPage.objects.count()
    main_news = NewsPage.objects.last()
    news = NewsPage.objects.all()[:num-1:-1]
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/newstack-kannada')
    return render(request, 'iiitdsite/newstack(kannada).html', {'acad_link': acad_link, 'main_news': main_news,'news': news, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def placements(request):
    companies_active = Placements.objects.all()[:4:-1]
    lst = len(companies_active)
    iters = range(1, (lst//4) + 1)
    companies = Placements.objects.all()[::-1]
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/placements')
    return render(request, 'iiitdsite/placements.html', {'lst': lst, 'iters': iters, 'companies': companies, 'companies_active': companies_active, 'acad_link': acad_link, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def placementshindi(request):
    companies_active = Placements.objects.all()[:4:-1]
    lst = len(companies_active)
    iters = range(1, (lst // 4) + 1)
    companies = Placements.objects.all()[::-1]
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/placements-hindi')
    return render(request, 'iiitdsite/placemnets(hindi).html', {'lst': lst, 'iters': iters, 'companies': companies, 'companies_active': companies_active, 'acad_link': acad_link, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def placementskannada(request):
    companies_active = Placements.objects.all()[:4:-1]
    lst = len(companies_active)
    iters = range(1, (lst // 4) + 1)
    companies = Placements.objects.all()[::-1]
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/placements-kannada')
    return render(request, 'iiitdsite/placements(kannada).html', {'lst': lst, 'iters': iters, 'companies': companies, 'companies_active': companies_active, 'acad_link': acad_link, 'currilink': currilink,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def research(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    points = ResearchPoints.objects.all()
    students = ResearchStudents.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/research')
    return render(request, 'iiitdsite/research.html', {'acad_link': acad_link, 'currilink': currilink,'points': points, 'students': students, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def researchhindi(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    points = ResearchPoints.objects.all()
    students = ResearchStudents.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/research-hindi')
    return render(request, 'iiitdsite/researchhindi.html', {'acad_link': acad_link, 'currilink': currilink,'points': points, 'students': students,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def researchkannada(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    points = ResearchPoints.objects.all()
    students = ResearchStudents.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/research-kannada')
    return render(request, 'iiitdsite/researchkannada.html', {'acad_link': acad_link, 'currilink': currilink,'points': points, 'students': students,'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def administration(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    administration = Administration.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/administration')
    return render(request, 'iiitdsite/administration.html', {'administration': administration, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def administrationhindi(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    administration = Administration.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/administration-hindi')
    return render(request, 'iiitdsite/administration(hindi).html', {'administration': administration, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def administrationkannda(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    administration = Administration.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/administration-kannada')
    return render(request, 'iiitdsite/administration(kannda).html', {'administration': administration, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def admissions(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/admissions')
    return render(request, 'iiitdsite/admission.html', {'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def admissionshindi(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/admissions-hindi')
    return render(request, 'iiitdsite/admission(hindi).html', {'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def admissionskannda(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/admissions-kannada')
    return render(request, 'iiitdsite/admission(kannada).html', {'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def BOG(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    chairperson = BOGChairperson.objects.last()
    members = BOGMembers.objects.all()[::-1]
    nonmembers = BOGNonMembers.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/board-of-governers')
    return render(request, 'iiitdsite/board_of_governers.html', {'chairperson': chairperson, 'members' : members, 'nonmembers': nonmembers,'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def BOGhindi(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    chairperson = BOGChairperson.objects.last()
    members = BOGMembers.objects.all()[::-1]
    nonmembers = BOGNonMembers.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/board-of-governers-hindi')
    return render(request, 'iiitdsite/board_of_governers(hindi).html', {'chairperson': chairperson, 'members' : members, 'nonmembers': nonmembers,'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def BOGkannada(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    chairperson = BOGChairperson.objects.last()
    members = BOGMembers.objects.all()[::-1]
    nonmembers = BOGNonMembers.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/board-of-governers-kannda')
    return render(request, 'iiitdsite/board_of_governers(kannada).html', {'chairperson': chairperson, 'members' : members, 'nonmembers': nonmembers,'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def financecommittee(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    chairperson = BOGChairperson.objects.last()
    members = FinanceCommitteeMembers.objects.all()[::-1]
    nonmembers = BOGNonMembers.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/finance-committee')
    return render(request, 'iiitdsite/finance_committee.html', {'chairperson': chairperson, 'nonmembers': nonmembers, 'members': members, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def financecommitteehindi(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    chairperson = BOGChairperson.objects.last()
    members = FinanceCommitteeMembers.objects.all()[::-1]
    nonmembers = BOGNonMembers.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/finance-committee-hindi')
    return render(request, 'iiitdsite/finance_committee(hindi).html', {'chairperson': chairperson, 'nonmembers': nonmembers, 'members': members, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})

def financecommitteekannada(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    chairperson = BOGChairperson.objects.last()
    members = FinanceCommitteeMembers.objects.all()[::-1]
    nonmembers = BOGNonMembers.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/finance-committee-kannada')
    return render(request, 'iiitdsite/finance_committee(kannada).html', {'chairperson': chairperson, 'nonmembers': nonmembers, 'members': members, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def senate(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    members = SenateMembers.objects.all()[::-1]
    chairperson = SenateChairperson.objects.last()
    nonmembers = BOGNonMembers.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/senate')
    return render(request, 'iiitdsite/senate.html', {'chairperson': chairperson, 'nonmembers': nonmembers, 'members': members, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def senatehindi(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    members = SenateMembers.objects.all()[::-1]
    chairperson = SenateChairperson.objects.last()
    nonmembers = BOGNonMembers.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/senate-hindi')
    return render(request, 'iiitdsite/senate(hindi).html', {'chairperson': chairperson, 'nonmembers': nonmembers, 'members': members, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def senatekannada(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    members = SenateMembers.objects.all()[::-1]
    chairperson = SenateChairperson.objects.last()
    nonmembers = BOGNonMembers.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/senate-kannada')
    return render(request, 'iiitdsite/senate(kannada).html', {'chairperson': chairperson, 'nonmembers': nonmembers, 'members': members, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def staff(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    members = Staff.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/staff')
    return render(request, 'iiitdsite/staff.html', {'members': members, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def staffhindi(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    members = Staff.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/staff-hindi')
    return render(request, 'iiitdsite/staff(hindi).html', {'members': members, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def staffkannada(request):
    links = ugcselinks.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    members = Staff.objects.all()[::-1]
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/staff-kannada')
    return render(request, 'iiitdsite/staff(kannada).html', {'members': members, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel, 'temp_fah': temp_fah, 'links': links,})


def ugcse(request):
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    links = ugcselinks.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/ug-cse')
    return render(request, 'iiitdsite/undergraduate_cse.html',
                  {'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel,
                   'temp_fah': temp_fah, 'links': links})


def ugcsehindi(request):
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    links = ugcselinks.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/ug-cse-hindi')
    return render(request, 'iiitdsite/undergraduate_cse(hindi).html',
                  {'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel,
                   'temp_fah': temp_fah, 'links': links})


def ugcsekannada(request):
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    links = ugcselinks.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/ug-cse-kannada')
    return render(request, 'iiitdsite/undergraduate_cse(kannada).html',
                  {'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel,
                   'temp_fah': temp_fah, 'links': links})


def phd(request):
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    links = phdlinks.objects.last()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/phd')
    return render(request, 'iiitdsite/Phd.html',
                  {'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel,
                   'temp_fah': temp_fah, 'links': links})


def phdhindi(request):
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    links = phdlinks.objects.last()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/phd-hindi')
    return render(request, 'iiitdsite/Phd(hindi).html',
                  {'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel,
                   'temp_fah': temp_fah, 'links': links})


def phdkannada(request):
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    links = phdlinks.objects.last()
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/phd-kannada')
    return render(request, 'iiitdsite/Phd(kannada).html',
                  {'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel,
                   'temp_fah': temp_fah, 'links': links})


def faqs(request):
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/faq')
    return render(request, 'iiitdsite/FAQ.html',
                  {'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel,
                   'temp_fah': temp_fah})

def faqshindi(request):
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/faq-hindi')
    return render(request, 'iiitdsite/FAQ(hindi).html',
                  {'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel,
                   'temp_fah': temp_fah})


def faqskannada(request):
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/faq')
    return render(request, 'iiitdsite/FAQ(kannada).html',
                  {'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel,
                   'temp_fah': temp_fah})


def Scholarships(request):
    links = Scholarship.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/scholarship')
    return render(request, 'iiitdsite/scholarship.html',
                  {'links': links, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel,
                   'temp_fah': temp_fah})


def Scholarshipshindi(request):
    links = Scholarship.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/scholarship-hindi')
    return render(request, 'iiitdsite/scholarship(hindi).html',
                  {'links': links, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel,
                   'temp_fah': temp_fah})


def Scholarshipskannada(request):
    links = Scholarship.objects.last()
    acad_link = AcademicCalLink.objects.get(id=1)
    currilink = CurriculumLink.objects.get(id=1)
    if request.method == 'POST':
        email = request.POST.get('email')
        emailid = NewsLetterEmail.objects.create(email_id=email)
        NewsLetterEmail.save(emailid)
        return redirect('/scholarship-kannada')
    return render(request, 'iiitdsite/scholarship(kannada).html',
                  {'links': links, 'acad_link': acad_link, 'currilink': currilink, 'temp_cel': temp_cel,
                   'temp_fah': temp_fah})


def chatbot(request):
    return render(request, 'iiitdsite/chatbot_abd.html')