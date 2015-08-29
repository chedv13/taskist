from django.core.management import BaseCommand
from taskist.blog.models import Post


class Command(BaseCommand):
    help = "Remove old posts (> 10 days)"

    def handle(self, *args, **options):
        print "Post count: %i" % (Post.objects.count())
