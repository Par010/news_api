from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string


def custom_slugify(source_field, suffix=False):
    """
    Using django util methods create a slug.
    Append a random string at the end of the slug if necessary for making it unique
    """

    # slugify the source_field passed to the function
    new_slug = slugify(source_field)

    if suffix:
        # get a random string of length 10
        random_str = get_random_string(length=10)

        # the new_slug and random_str is concatenated
        new_slug = "{0}-{1}".format(new_slug, random_str)

    return new_slug
