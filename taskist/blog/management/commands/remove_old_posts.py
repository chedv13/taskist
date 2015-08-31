from django.core.management import BaseCommand
from taskist.blog.models import Post
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = "Remove old posts (> 10 days)"

    def handle(self, *args, **options):
        ten_days_ago = datetime.now() - timedelta(days=10)

        Post.objects.filter(created_at__lte=ten_days_ago).delete()
