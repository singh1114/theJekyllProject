from django.core.exceptions import ObjectDoesNotExist


class BaseDbIO:
    """
    Base database input output to setup every database I/O operations.
    class is DEPRECATED and use of AbstractBaseDbIO is encouraged.
    """
    def get_obj(self, kwargs):
        """
        This method is used to get the database object
        """
        try:
            return self.model_name.objects.get(**kwargs)
        except ObjectDoesNotExist:
            return None

    def save_db_instance(self, kwargs):
        """
        save/create instances of ORM into the database
        """
        self.model_name.objects.create(**kwargs)

    def update_obj(self, model_obj, kwargs):
        """
        update the ORM instance
        """
        for key, value in kwargs.items():
            setattr(model_obj, key, value)
        return model_obj.save()

class AbstractBaseDbIO(object):
    def __init__(self, model_name):
        self.model_name = model_name

    def get_obj(self, kwargs):
        """
        This method is used to get the database object
        """
        try:
            return self.model_name.objects.get(**kwargs)
        except ObjectDoesNotExist:
            return None

    def create_obj(self, kwargs):
        """
        save/create instances of ORM into the database
        """
        return self.model_name.objects.create(**kwargs)

    def update_obj(self, model_obj, kwargs):
        """
        update the ORM instance
        """
        for key, value in kwargs.items():
            setattr(model_obj, key, value)
        return model_obj.save()
