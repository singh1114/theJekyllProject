import os


class FileHandler:
    """
    All the operations related to files can be handled here
    """
    def __init__(self, file_path, file_name=None):
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

    def delete_file(self):
        """
        delete the whole file using this method
        """
        os.remove('/'.join([self.file_path, self.file_name]))

    def read_wrapped_content(self, content, wrapper):
        """
        This method is used to read wrapped content separately.
        return the content between wrapper.
        content and wrapper are two requirements.
        content: --- some random string --- some other random string
        wrapper: '---'
        Better to call self.read_file first.
        """
        wrapper_len = len(wrapper)
        first_occurence = content.find(wrapper)
        second_occurence = content[first_occurence + wrapper_len:].find(
            wrapper)
        partition = first_occurence + second_occurence + (2 * wrapper_len)
        wrapped_content = content[wrapper_len:partition - wrapper_len]
        rest_content = content[partition:]
        return wrapped_content, rest_content

    def read_all(self, extension, exception_list):
        """
        read all files that we want at any time.
        we have to pass the extension and exception_list.
        exception_list will contain the list of all the files
        that should'nt be scanned.
        extension: 'markdown'
        exception_list: ('README', '404')
        """
        for file in os.listdir(self.path):
            if file.endswith('.'.join(['', extension])):
                if file not in exception_list:
                    content = self.read_file(file)
                    head_data, body_content = self.read_wrapped_content(
                        content, '---')
