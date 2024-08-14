from django.apps import AppConfig


class ProductsConfig(AppConfig): # я не знал что этот подкласс определяется "из коробки".
    # пока что не имею понимания ни зачем он нужен, ни правильно ли я его определил
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
    verbose_name = 'Товары'
