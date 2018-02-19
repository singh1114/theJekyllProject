class FormHandler:
    """
    We would use this class for handling all the form events
    """
    def __init__(self, request, form_class, form_fields):
        self.request = request
        self.form_class = form_class
        self.form_fields = form_fields

    def handle_post_fields(self):
        """
        This function is used to post the form fields
        """
        # FIXME this function will not work anyway
        if(self.form_class(self.request.POST).is_valid()):
            fields_data = [self.request.POST.field
                           for field in self.form_fields]
            return fields_data
