# django level imports
from django.db import models
from django.db import transaction
from django.db import IntegrityError

# project level imports
from publishers.utils.modelutils import custom_slugify


class Publisher(models.Model):
    """
    This class handles Publisher class models.py
    """
    name = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):

        self.name = self.name.title() if self.name else self.name

        if not self.slug:
            # if slug doesn't exist pass the source_field and suffix=False to custom_slugify function
            self.slug = custom_slugify(source_field=self.name, suffix=False)

        try:
            """
            While saving, it we have a duplicate combination of name and slug
            Since we have added an IntegrityError check, we will have an exception raised
            """
            # This will prevent the purposefully-thrown exception from breaking the entire unittest's transaction.
            with transaction.atomic():
                # since unique combination of source_field and slug exists, call save method
                super(Publisher, self).save(*args, **kwargs)

        except IntegrityError:
            """
            after catching the exception, we will generate another slug but this time we will
            suffix  it with a random string at the end of the slug to make it unique and try saving it again
            """

            # since unique combination of source_field and slug doesn't exist,
            # pass suffix=True to add random_str to make it unique
            self.slug = custom_slugify(source_field=self.name, suffix=True)
            super(Publisher, self).save(*args, **kwargs)

    def __str__(self):
        return "{0}-{1}".format(self.id, self.name)

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'
