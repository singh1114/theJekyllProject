class FileHandler:
    """
    All the operations related to files can be handled here
    """
    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name

    def read_file(self):
        """
        Read the content of the file
        """
        with open('/'.join([self.file_path, self.file_name]), 'r') as file:
            return file.read()

    def rewrite_file(self, content):
        """
        re-write the whole file
        """
        with open('/'.join([self.file_path, self.file_name]), 'w') as file:
            return file.write(content)

    def wrap_content(self, wrapper, content):
        """
        This function is used to wrap content with a wrapper
        """
        return '\n'.join([wrapper, content, wrapper])
