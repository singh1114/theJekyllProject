from ruamel import yaml


class YAMLHandler:
    def __init__(self):
        pass

    def read_yaml_file(self, file_path, full_file=False):
        """
        This method will be used to read yml content from files.
        If full file is true then we will read full file otherwise we
        will read the content between --- and ---
        """
        if full_file:
            with open(file_path, 'r') as file:
                content = file.read()
            return self.read_yaml(content)
        # FIXME write the code about how to handle full_file=False case

    def read_yaml(self, content):
        """
        This method can be used to read yaml from given content. Throws
        if the content is not valid.
        """
        return yaml.load(
            content, Loader=yaml.RoundTripLoader, preserve_quotes=True)

    def write_yaml(self, file_path, yaml_dict):
        """
        This method is used to write yaml to some file
        :return:
        """
        with open(file_path, 'w') as yaml_file:
            return yaml.dump(
                yaml_dict, yaml_file, Dumper=yaml.RoundTripDumper
            )

    def change_yaml(self, yaml_dict, change_dict):
        """
        This method will be used to change the yml_data
        """
        return yaml_dict.update(**change_dict)
