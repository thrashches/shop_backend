from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='Категория'
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Цена'
    )

    image = models.ImageField(
        upload_to='product_images',
        default=None,
        blank=True,
        null=True,
        verbose_name='Фотография товара'
    )

    info = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание'
    )

    weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name='Вес'
    )

    energy_value = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name='Энергетическая ценность'
    )

    time_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата/время создания'
    )

    time_updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата/время обновления'
    )

    is_published = models.BooleanField(verbose_name='Отображён на сайте')

    is_new = models.BooleanField(verbose_name='Есть бейдж "Новинка"')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-time_updated']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
