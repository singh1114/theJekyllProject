class BaseDbIO:
    """
    Base database input output to setup every database I/O operations.
    """
    def __init__(self, model_name):
        self.model_name = model_name

    def save_db_instance(self, kwargs):
        """
        save/create instances of ORM into the database
        """
        self.model_name.create(**kwargs)
