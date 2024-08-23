import datetime
import logging

from django.core.mail import EmailMultiAlternatives
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django_apscheduler import util
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django.contrib.auth.models import User

from app.models import *

logger = logging.getLogger(__name__)


# def my_job():
#     users = Message.objects.filter(User)
#     today = datetime.datetime.now()
#     last_week = today - datetime.timedelta(days=7)
#     messages = Message.objects.filter(dateMsg__gte=last_week)
#     html_content = render_to_string(
#         'daily_messages.html',
#         {
#             'link': f'http://127.0.0.1:8000/',
#             'posts': messages,
#         }
#     )
#     msg = EmailMultiAlternatives(
#         subject='Публикации за неделю',
#         body='',
#         from_email=None,
#         to=[users.email]
#     )
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()
def my_job():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Message.objects.filter(dateMsg__gte=last_week)
    authors = User.objects.filter()
    html_content = render_to_string(
        'daily_messages.html',
        {
            'link': f'http://127.0.0.1:8000/',
            'posts': posts,
        }
    )
    for auth in authors:
        msg = EmailMultiAlternatives(
            subject='Публикации за неделю',
            body='',
            from_email=None,
            to=[auth.email]
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age`
    from the database.
    It helps to prevent the database from filling up with old historical
    records that are no longer useful.

    :param max_age: The maximum length of time to retain historical
                    job execution records. Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(day_of_week="sun", hour="08", minute="00"),  # Every 10 seconds
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: 'delete_old_job_executions'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
