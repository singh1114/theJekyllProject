class FormHandler:
    """
    We would use this class for handling all the form events
    """
    def __init__(self, request, form_class):
        self.request = request
        self.form_class = form_class

    def handle_post_fields(self, fields):
        """
        This function is used to post the form fields
        """
        field_dict = {}
        if(self.form_class(self.request.POST).is_valid()):
            for key, value in self.request.POST.dict().items():
                if key == 'csrfmiddlewaretoken':
                    continue
                field_dict[key] = value

            return field_dict

    def load_initials(self, db_data):
        """
        This method will be used to load initial datasets from db
        """
        if db_data is None:
            return self.form_class
        return self.form_class(initial=db_data.__dict__)
