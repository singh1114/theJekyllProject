class ExtraHandler:
    def del_keys(self, main_dict, key_list):
        """
        This method will be used to del keys from the dictionary
        main_dict is the dictionary from where the keys will be deleted
        key_list is the list with the keys that are required to be deleted
        """
        for key in key_list:
            try:
                del(main_dict[key])
            except KeyError:
                continue

    def wrap_content(self, wrapper, content):
        """
        This function is used to wrap content with a wrapper
        """
        return '\n'.join([wrapper, content, wrapper])

    def join_content(self, arg_one, *args):
        """
        This function will be used to join the contents in the *args
        arg1 is the first argument followed by the multi numbers of args
        """
        for arg in args:
            arg_one = '\n'.join(arg_one, arg)
        return arg_one

    def file_name_f_title(self, title, extension):
        """
        Method used to create file name from title of the post
        """
        title = title.lower()
        title.replace(' ', '-')
        return '.'.join([title, extension])
