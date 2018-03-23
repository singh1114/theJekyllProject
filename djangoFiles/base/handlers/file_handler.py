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


class YMLFileHandler(FileHandler):
    """
    Special handler to read YML files
    """
    def return_yaml(self):
        file_content = self.read_file()
        # Change the file content to dict and return it
        # FIXME get the yaml
        return file_content.yaml

    def change_data(self, change_dict):
        """
        the particular data that you want to change in the yaml
        :param change_dict: the dict that will change the data
        :return: the changed dict
        """
        # FIXME complete this function
        return
