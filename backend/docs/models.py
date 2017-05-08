from django.db import models
from django.conf import settings

from taggit.managers import TaggableManager

from config.models import DatedModel

User = settings.AUTH_USER_MODEL


class Document(DatedModel):
    # Fields included: updated, created
    tags = TaggableManager()
    contributors = models.ManyToManyField(
        User,
        related_name='documents',
        blank=True,
    )


class Section(DatedModel):
    # Fields included: updated, created
    pass


class Comment(DatedModel):
    # Fields included: updated, created
    section = models.ForeignKey(Section)
    user = models.ForeignKey(User, related_name='comments')
