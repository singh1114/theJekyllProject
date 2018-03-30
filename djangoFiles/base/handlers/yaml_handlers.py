from ruamel import yaml

from django.core import settings


class YAMLHandler:
    def __init__(self):
        pass

    def read_yaml(self, content):
        """
        This method can be used to read yaml from given content. Throws 
        if the content is not valid.
        """
        return yaml.load(
            data, Loader=ruamel.yaml.RoundTripLoader, preserve_quotes=True)

    def write_yaml(self, file, yml_dict):
        """
        This method is used to write yaml to some file
        :return:
        """
        with open(os.path.join(settings.BASE_DIR, file), 'w') as yml_file:
            yaml.dump(yml_data, yml_file, Dumper=ruamel.yaml.RoundTripDumper)

    def change_yml(self, yml_dict, change_dict):
        """
        This method will be used to change the yml_data
        """
        return yml_dict.update(**change_dict)
