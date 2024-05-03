import logging
from django.db import migrations

logger = logging.getLogger(__name__)

def generate_superuser(apps, schema_editor):
    from django.contrib.auth import get_user_model

    USERNAME = "root"
    PASSWORD = "root1234"
    EMAIL = "root@example.com"

    user = get_user_model()

    if not user.objects.filter(username=USERNAME, email=EMAIL).exists():
        logger.info("Creating new superuser")
        admin = user.objects.create_superuser(
           username=USERNAME, password=PASSWORD, email=EMAIL
        )
        admin.save()
    else:
        logger.info("Superuser already created!")


class Migration(migrations.Migration):
   dependencies = [("core", "0001_initial")]

   operations = [migrations.RunPython(generate_superuser)]
