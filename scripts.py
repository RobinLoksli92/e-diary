import random


from datacenter.models import Mark, Chastisement, Lesson, Schoolkid, Commendation


def fix_marks(schoolkid):
    schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid)[0]
    child_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3])
    for child_mark in child_marks:
        child_mark.points = 5
        child_mark.save()


def remove_chastisements(schoolkid):
    schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid)[0]
    child_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    child_chastisements.delete()


def create_commendation(schoolkid, subject_title):
    texts = ['Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!']
    schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid)[0]
    kid_study_year = schoolkid.year_of_study
    kid_group_letter = schoolkid.group_letter
    kid_lessons = Lesson.objects.filter(year_of_study=kid_study_year, group_letter=kid_group_letter)
    certain_kid_lesson = kid_lessons.filter(subject__title=subject_title).order_by('?').first()
    Commendation.objects.create(
        schoolkid=schoolkid,
        teacher=certain_kid_lesson.teacher, 
        subject=certain_kid_lesson.subject,
        created=certain_kid_lesson.date,
        text=random.choice(texts)
        )