from django.db import models
from user_site.models import *
from user_site.forms import *
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class UserComment(models.Model):
    """Model for user comments"""
    content = models.TextField("Inhalt", max_length=5000, default="")
    error_appearance = models.ForeignKey(verbose_name=_("Error appearance"), to=ErrorAppearance, on_delete=models.CASCADE,
                                         default=None, blank=True)
    created_date = models.DateTimeField(verbose_name=_("create date"), auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("New user comment")
        verbose_name_plural = _("New user comments")


class CommentGroup(models.Model):
    """model for groups of semantic similar user comments"""
    error_appearance = models.ForeignKey(verbose_name=_("Error appearance"), to=ErrorAppearance, on_delete=models.CASCADE,
                                         default=None, blank=True)
    def __str__(self):
        return _("Group") + " " + str(self.pk)
    class Meta:
        verbose_name = _("Group of user comments")
        verbose_name_plural = _("Groups of user comments")


class Sentence(models.Model):
    """model for a sentence of a user comment"""
    name = models.TextField(verbose_name=_("Sentence"), max_length=5000, default="")
    content = models.TextField(verbose_name=_("Content"), max_length=5000, default="")
    group = models.ForeignKey(verbose_name=_("Group"), to=CommentGroup,on_delete=models.SET_NULL, null=True, blank=True)
    user_comment = models.ForeignKey(verbose_name=_("User comment"), to=UserComment, on_delete=models.CASCADE)

    def __str__(self):
       return self.name

    class Meta:
        verbose_name = _("Sentence")
        verbose_name_plural = _("Sentences")


class Keyword(models.Model):
    """model of a keyword of a sentence of a user comment"""
    lemma = models.TextField(verbose_name=_("Lemma"), max_length=5000, default="")
    sentence = models.ManyToManyField(verbose_name=_("Sentence"), to=Sentence)

    class Meta:
        verbose_name = _("Keyword")
        verbose_name_plural = _("Keywords")


class Threshold(models.Model):
    """pseudo model for the similarity threshold"""

    value = models.FloatField(verbose_name=_("Value"), validators=[MinValueValidator(0.1), MaxValueValidator(1.0)], default=0.7)

    class Meta:
        verbose_name = _("Similarity threshold")
        verbose_name_plural = _("Similarity threshold")


