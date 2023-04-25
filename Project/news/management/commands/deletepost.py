from django.core.management.base import BaseCommand
from news.models import Post, Category


class Command(BaseCommand):
    help = 'Подсказка вашей команды'
    missing_args_message = 'Недостаточно аргументов'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        self.stdout.readable()
        self.stdout.write('Подтвердите удаление: y/n')
        answer = input()

        if answer == 'y':
            category = Category.objects.get(name=options['category'])
            Post.objects.filter(postCategory=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Удаление выполнено'))
            return

        self.stdout.write(self.style.ERROR(f'Не удалось выполнить удаление'))
