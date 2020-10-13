from django.db import models


class FacultyPageInfo(models.Model):
    name = models.CharField(max_length=100)
    name_hindi = models.CharField(max_length=100)
    name_kannada = models.CharField(max_length=100)
    phd_info = models.CharField(max_length=100, blank=True)
    phd_info_hindi = models.CharField(max_length=100, blank=True)
    phd_info_kannada = models.CharField(max_length=100, blank=True)
    teaching_position = models.CharField(max_length=300)
    teaching_position_hindi = models.CharField(max_length=300)
    teaching_position_kannada = models.CharField(max_length=300)
    linkedin_link = models.CharField(max_length=300)
    email_id = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Faculty/', blank=True, null=True)

    def __str__(self):
        return self.name


class NewsLetterEmail(models.Model):
    email_id = models.CharField(max_length=100)

    def __str__(self):
        return self.email_id


class Events(models.Model):
    event_name = models.CharField(max_length=100)
    event_name_hindi = models.CharField(max_length=100)
    event_name_kannada = models.CharField(max_length=100)
    date = models.DateField()
    description = models.CharField(max_length=1000)
    description_hindi = models.CharField(max_length=1000)
    description_kannada = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='EventsCover/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.event_name


class images(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Events/%Y/%m/%d', blank=True, null=True)
    image_name = models.CharField(max_length=100)

    def __str__(self):
        return self.image_name


class About(models.Model):
    director_image_link = models.ImageField(upload_to='Director/', blank=True, null=True)
    chairperson_image_link = models.ImageField(upload_to='Chairperson/', blank=True, null=True)


class OurFamilyLink(models.Model):
    name = models.CharField(max_length=50)
    name_hindi = models.CharField(max_length=50)
    name_kannada = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    link_hindi = models.CharField(max_length=200)
    link_kannada = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AboutUsTestimonial(models.Model):
    image = models.ImageField(upload_to='About/', blank=True, null=True)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    name_hindi = models.CharField(max_length=50)
    position_hindi = models.CharField(max_length=50)
    description_hindi = models.CharField(max_length=300)
    name_kannada = models.CharField(max_length=50)
    position_kannada = models.CharField(max_length=50)
    description_kannada = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class AcademicsCSE(models.Model):
    description = models.CharField(max_length=3000)
    description_hindi = models.CharField(max_length=3000)
    description_kannada = models.CharField(max_length=3000)
    academic_calendar_link = models.CharField(max_length=200)
    curriculum_link = models.CharField(max_length=200)


class AcademicsECE(models.Model):
    description = models.CharField(max_length=3000)
    description_hindi = models.CharField(max_length=3000)
    description_kannada = models.CharField(max_length=3000)
    academic_calendar_link = models.CharField(max_length=200)
    curriculum_link = models.CharField(max_length=200)


class Academics(models.Model):
    cse_image_link = models.CharField(max_length=200)
    ece_image_link = models.CharField(max_length=200)
    academic_calendar_link = models.CharField(max_length=200)


class ResearchPoints(models.Model):
    point = models.CharField(max_length=300)
    point_hindi = models.CharField(max_length=300)
    point_kannada = models.CharField(max_length=300)


class ResearchStudents(models.Model):
    name = models.CharField(max_length=100)
    name_hindi = models.CharField(max_length=100)
    name_kannada = models.CharField(max_length=100)
    image_link = models.ImageField(upload_to='ResearchStudents/', blank=True, null=True)

    def __str__(self):
        return self.name


class CurriculumLink(models.Model):
    cse_link = models.CharField(max_length=200)
    ece_link = models.CharField(max_length=200)


class NewsPage(models.Model):
    news_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='News/%Y/%m/%d', blank=True, null=True)
    headline = models.CharField(max_length=300)
    headline_hindi = models.CharField(max_length=300)
    headline_kannada = models.CharField(max_length=300)
    description = models.CharField(max_length=3000)
    description_hindi = models.CharField(max_length=3000)
    description_kannada = models.CharField(max_length=3000)
    news_type = models.CharField(max_length=50)


class CampusPageDetails(models.Model):
    title = models.CharField(max_length=100)
    title_hindi = models.CharField(max_length=100)
    title_kannada = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    description_hindi = models.CharField(max_length=3000)
    description_kannada = models.CharField(max_length=3000)
    image = models.ImageField(upload_to='Campus/', blank=True, null=True)

    def __str__(self):
        return self.title


class CampusPageGallery(models.Model):
    title = models.ForeignKey(CampusPageDetails, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='CampusGallery/', blank=True, null=True)


class HomePageUpcomingEvents(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.CharField(max_length=1000)
    description_hindi = models.CharField(max_length=1000)
    description_kannada = models.CharField(max_length=1000)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='UpcomingEventsCover/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.title


class Placements(models.Model):
    logo = models.ImageField(upload_to='PlacementCompanyLogo/', blank=True, null=True)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class AcademicCalLink(models.Model):
    acad_link = models.CharField(max_length=200)


class Administration(models.Model):
    name = models.CharField(max_length=100)
    name_hindi = models.CharField(max_length=100)
    name_kannada = models.CharField(max_length=100)
    position = models.CharField(max_length=300)
    position_hindi = models.CharField(max_length=300)
    position_kannada = models.CharField(max_length=300)
    image = models.ImageField(upload_to='Administration/', blank=True, null=True)

    def __str__(self):
        return self.name


class BOGChairperson(models.Model):
    name = models.CharField(max_length=100)
    name_hindi = models.CharField(max_length=100)
    name_kannada = models.CharField(max_length=100)
    position = models.CharField(max_length=300)
    position_hindi = models.CharField(max_length=300)
    position_kannada = models.CharField(max_length=300)
    image = models.ImageField(upload_to='Chairperson/', blank=True, null=True)

    def __str__(self):
        return self.name


class BOGMembers(models.Model):
    name = models.CharField(max_length=100)
    name_hindi = models.CharField(max_length=100)
    name_kannada = models.CharField(max_length=100)
    position = models.CharField(max_length=300)
    position_hindi = models.CharField(max_length=300)
    position_kannada = models.CharField(max_length=300)
    image = models.ImageField(upload_to='BOGMembers/', blank=True, null=True)

    def __str__(self):
        return self.name


class BOGNonMembers(models.Model):
    name = models.CharField(max_length=100)
    name_hindi = models.CharField(max_length=100)
    name_kannada = models.CharField(max_length=100)
    position = models.CharField(max_length=300)
    position_hindi = models.CharField(max_length=300)
    position_kannada = models.CharField(max_length=300)
    image = models.ImageField(upload_to='BOGNonMembers', blank=True, null=True)

    def __str__(self):
        return self.name


class FinanceCommitteeMembers(models.Model):
    name = models.CharField(max_length=100)
    name_hindi = models.CharField(max_length=100)
    name_kannada = models.CharField(max_length=100)
    position = models.CharField(max_length=300)
    position_hindi = models.CharField(max_length=300)
    position_kannada = models.CharField(max_length=300)
    image = models.ImageField(upload_to='FCMembers/', blank=True, null=True)

    def __str__(self):
        return self.name


class SenateChairperson(models.Model):
    name = models.CharField(max_length=100)
    name_hindi = models.CharField(max_length=100)
    name_kannada = models.CharField(max_length=100)
    position = models.CharField(max_length=300)
    position_hindi = models.CharField(max_length=300)
    position_kannada = models.CharField(max_length=300)
    image = models.ImageField(upload_to='Chairperson', blank=True, null=True)

    def __str__(self):
        return self.name


class SenateMembers(models.Model):
    name = models.CharField(max_length=100)
    name_hindi = models.CharField(max_length=100)
    name_kannada = models.CharField(max_length=100)
    position = models.CharField(max_length=300)
    position_hindi = models.CharField(max_length=300)
    position_kannada = models.CharField(max_length=300)
    image = models.ImageField(upload_to='SenateMembers/', blank=True, null=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    name_hindi = models.CharField(max_length=100)
    name_kannada = models.CharField(max_length=100)
    position = models.CharField(max_length=300)
    position_hindi = models.CharField(max_length=300)
    position_kannada = models.CharField(max_length=300)
    image = models.ImageField(upload_to='Staff/', blank=True, null=True)

    def __str__(self):
        return self.name


class ugcselinks(models.Model):
    jossa_link = models.CharField(max_length=200)
    csab_link = models.CharField(max_length=200)
    course_seat_matrix = models.CharField(max_length=200)
    admission_checklist = models.CharField(max_length=200)
    fee_structure = models.CharField(max_length=200)
    sbi_collect = models.CharField(max_length=200)
    instructions_sbi_collect = models.CharField(max_length=200)
    academic_regulations = models.CharField(max_length=200)
    scholarships_bank_loans = models.CharField(max_length=200)
    policy = models.CharField(max_length=200)


class phdlinks(models.Model):
    advertisement = models.CharField(max_length=200)
    click_here_to_apply = models.CharField(max_length=200)
    fee_structure = models.CharField(max_length=200)
    sbi_collect = models.CharField(max_length=200)
    instructions_sbi_collect = models.CharField(max_length=200)
    academic_regulations = models.CharField(max_length=200)
    scholarships_bank_loans = models.CharField(max_length=200)
    policy = models.CharField(max_length=200)


class Scholarship(models.Model):
    education_loan_application = models.CharField(max_length=200)
    checklist = models.CharField(max_length=200)


class Alert(models.Model):
    notice = models.CharField(max_length=200)
    news_name = models.CharField(max_length=200)


class Jobs(models.Model):
    prof_link = models.CharField(max_length=200)
    asso_prof_link = models.CharField(max_length=200)
    assi_prof_link = models.CharField(max_length=200)
    project = models.CharField(max_length=200)
    tech_assistant = models.CharField(max_length=200)
    assi_registrar = models.CharField(max_length=200)
    super_hrm = models.CharField(max_length=200)
    super_accounts = models.CharField(max_length=200)
    office_assistant = models.CharField(max_length=200)
    audit_officer = models.CharField(max_length=200)


class HomePageGallery(models.Model):
    image = models.ImageField(upload_to='Events/%Y/%m/%d', blank=True, null=True)