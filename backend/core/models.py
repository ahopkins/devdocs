from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# from . import emails


class User(AbstractUser):
    token_last_expired = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.get_full_name()

    def get_short_name(self):
        if self.first_name:
            if self.last_name:
                names = (self.first_name, self.last_name)
                return "".join([n[0] for n in names]).upper()
            else:
                return self.first_name
        else:
            return "N/A"

    def get_full_name(self):
        if self.first_name:
            if self.last_name:
                return " ".join([n for n in (self.first_name, self.last_name)])
            else:
                return self.first_name
        else:
            return "N/A"

    def get_display_name(self):
        if self.first_name and self.last_name:
            return "{}. {}".format(self.first_name[0], self.last_name)
        return self.username

    def save(self, *args, **kwargs):
        new_user = True if not self.pk else False

        super().save(*args, **kwargs)

        if new_user:
            self.is_active = True
            password = User.objects.make_random_password(length=18)
            self.set_password(password)
            self.save()
            # emails.UserRegistrationEmail(self, password=password).send()


class UserPreferences(models.Model):
    user = models.OneToOneField(User, related_name="preferences")


def create_user_preferences(sender, instance, created, **kwargs):
    if created:
        UserPreferences.objects.create(user=instance)


models.signals.post_save.connect(create_user_preferences, sender=User)
