from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from django.db import IntegrityError


class BaseDbIO:
    """
    Base database input output to setup every database I/O operations.
    """
    def save_db_instance(self, kwargs):
        """
        save/create instances of ORM into the database
        """
        self.model_name.objects.create(**kwargs)


class AbstractBaseDbIO(object):
    def __init__(self, model_name):
        self.model_name = model_name

    def get_or_filter(self, kwargs):
        """
        This method is used to either get or filter the
        """
        try:
            return self.model_name.objects.get(**kwargs)
        except MultipleObjectsReturned:
            return self.model_name.objects.filter(**kwargs)
        except ObjectDoesNotExist:
            # FIXME This needs to be evaluated
            return ''

    def create_or_update(self, kwargs, model_obj=None):
        """
        save/create instances of ORM into the database
        """
        try:
            self.model_name.objects.create(**kwargs)
        except IntegrityError:
            model_obj = model_obj(**kwargs)
            model_obj.save()

