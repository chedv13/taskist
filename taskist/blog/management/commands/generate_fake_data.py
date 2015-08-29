# coding=utf-8
from django.core.management import BaseCommand
from faker import Faker
from taskist.users.models import User
from django.core.files import File
import os
import random
from django.conf import settings


class Command(BaseCommand):
    help = "Generate fake data"

    def add_arguments(self, parser):
        parser.add_argument('model_name', nargs='+', type=str)

    def handle(self, *args, **options):
        fake = Faker()
        model_name = options['model_name'][0]

        # Генерацию пользователей надо вынести в пакет с пользователями
        if model_name == 'User':
            for _ in range(0, 100):
                name = fake.name()
                split_name = name.split(' ')
                dir_path = str(settings.ROOT_DIR) + '/media/images/'
                image = File(open(dir_path + random.choice(os.listdir(dir_path)), 'r'))

                # Password for testing
                user = User(first_name=split_name[0], last_name=split_name[1], name=name, email=fake.email(),
                            avatar=image, username='user' + str(_))
                user.set_password(name)
                user.save()
        elif model_name == 'Post':
            from taskist.blog.models import Post

            dir_path = str(settings.ROOT_DIR) + '/media/images/'
            image = File(open(dir_path + random.choice(os.listdir(dir_path)), 'r'))

            for _ in range(0, 1000):
                post = Post(title=fake.text(max_nb_chars=100), content=fake.text(max_nb_chars=500),
                            user=User.objects.order_by('?').first(), image=image)

                post.save()
        else:
            print 'Model not defined in generator'
