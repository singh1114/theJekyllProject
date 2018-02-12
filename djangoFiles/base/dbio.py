class BaseDbIO:
    """
    Base database input output to setup every database I/O operations.
    """
    def save_db_instance(self, kwargs):
        """
        save/create instances of ORM into the database
        """
        self.model_name.objects.create(**kwargs)
