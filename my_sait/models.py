from django.db import models
from django.contrib.auth.models import User, AbstractUser

FILTER_CHOICES = (
    (3, 231),
    (4, 232),
    (1, 331),
    (2, 332),
)


class Groups(models.Model):
    """Группы"""
    code = models.IntegerField("Код группы", default=None, unique=False, blank=True, null=True)

    def __str__(self):
        return str(self.code)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = 'Группы'


class UserProfile(AbstractUser):
    """Пользователи"""
    name = models.CharField('Имя', max_length=100)
    surname = models.CharField('Фамилия', max_length=100)
    username = models.CharField(blank=True, null=True, max_length=150)
    group = models.ForeignKey(Groups, verbose_name='Группа', unique=False, blank=True, null=True,
                              on_delete=models.PROTECT)
    email = models.EmailField('Почта', max_length=100, unique=True)
    password1 = models.CharField('Пароль1', max_length=100)
    password2 = models.CharField('Пароль2', max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'username', 'group']

    def __str__(self):
        return str(self.name + ' ' + self.surname)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'


class Items(models.Model):
    """Предметы"""
    name = models.CharField("Название предмета", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = 'Предметы'


class Marks(models.Model):
    """Оценки"""
    date = models.DateField('Дата')
    items_code = models.ForeignKey(Items, verbose_name="Предмет", on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, verbose_name="Группа", unique=False, blank=True, null=True,
                              on_delete=models.CASCADE)
    users_code = models.ForeignKey(UserProfile, verbose_name="Код пользователя", on_delete=models.CASCADE)
    mark = models.IntegerField('Оценка')
    comment = models.CharField('Комментарий', max_length=250, blank=True, default='')

    def __str__(self):
        return str(self.users_code) + " | " + str(self.date) + " | " + str(self.mark)

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = 'Оценки'


class TrpoLectures(models.Model):
    """Лекции"""
    file = models.FileField("Файл", upload_to='trpo/lectures')
    name = models.CharField("Имя лекции", max_length=100)
    items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)
    date = models.DateField('Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ТРПО Лекция"
        verbose_name_plural = 'ТРПО Лекции'


class PP0201Lectures(models.Model):
    """Лекции"""
    file = models.FileField("Файл", upload_to='pp0201/lectures')
    name = models.CharField("Имя лекции", max_length=100)
    items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)
    date = models.DateField('Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ПП.02.01. Лекция"
        verbose_name_plural = 'ПП.02.01. Лекции'


class PP0102Lectures(models.Model):
    """Лекции"""
    file = models.FileField("Файл", upload_to='pp0102/lectures')
    name = models.CharField("Имя лекции", max_length=100)
    items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)
    date = models.DateField('Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ПП.01.02. Лекция"
        verbose_name_plural = 'ПП.01.02. Лекции'


class TrpoPractices(models.Model):
    """Практики"""
    file = models.FileField("Файл", upload_to='trpo/practices')
    name = models.CharField("Имя лекции", max_length=100)
    items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)
    date = models.DateField('Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ТРПО Практика"
        verbose_name_plural = 'ТРПО Практики'


class PP0201Practices(models.Model):
    """Практики"""
    file = models.FileField("Файл", upload_to='pp0201/practices')
    name = models.CharField("Имя лекции", max_length=100)
    items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)
    date = models.DateField('Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ПП.02.01. Практика"
        verbose_name_plural = 'ПП.02.01. Практики'


class PP0102Practices(models.Model):
    """Практики"""
    file = models.FileField("Файл", upload_to='pp0102/practices')
    name = models.CharField("Имя лекции", max_length=100)
    items_code = models.ForeignKey(Items, verbose_name="Код предмета", on_delete=models.CASCADE)
    date = models.DateField('Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ПП.01.02. Практика"
        verbose_name_plural = 'ПП.01.02. Практики'
