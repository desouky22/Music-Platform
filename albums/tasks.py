from time import sleep
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from artists.models import Artist


@shared_task()
def sending_emails(artist_id):
    artist = Artist.objects.get(id=artist_id)
    artist_email = artist.user.email
    print("Sending emails")

    send_mail(
        subject="Congrats",
        message="We r so happy for ur new Album !",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[artist_email],
    )

    return None
