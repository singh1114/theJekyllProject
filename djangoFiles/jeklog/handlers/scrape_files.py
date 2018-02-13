import re

from markdown2 import Markdown

class FileScraper:
    def __init__(self, regex, file_data):
        self.regex = regex
        self.file_data = file_data

    def scrape_head_body(self, file_data):
        """
        scrape head content of the file
        head content is defined as the content between --- and --- everything
        after that is body.
        """
        return_dict = {}
        first_occurence = file_data.find('---')
        second_occurence = file_data[first_occurence+3:].find('---')
        return_dict['head'] = file_data[first_occurence:(first_occurence+
                                        second_occurence+6)]
        return_dict['body'] = file_data[first_occurence+second_occurence+6:]
        return return_dict

    def find_in_content(self, regex, file_data):
        """
        Find something in the content and return things accordingly
        """
        # FIXME try/catch this.
        try:
            data_found = re.findall(regex, file_data)
            return data_found[0].split(':')[1].strip()
        except IndexError:
            return ''

    def find_multi_line_content(self):
        """
        find and return multi line values in file_data with regex

        expected input:
            regex = exclude:

            file_data = {
                name: something
                code: something
                exclude:
                    - Real-job
                    - README
            }
        expected output:
            ['Real-job', 'README']
        """
        return_list = []
        file_data = self.file_data.split('\n')
        iterator = iter(file_data)
        line = next(iterator)

        # Try to find regex in the line
        while True:
            if re.search(self.regex, line):
                break
            else:
                line = next(iterator)

        # When you find it find  and return the list of options
        while True:
            line = next(iterator).strip()
            if line[:1] is '-':
                return_list.append(line.split(' ')[1])
            else:
                break
        return return_list

    def join_dicts(self, dict_one, dict_two):
        """
        This method is used to join to dictionaries together
        """
        #import ipdb; ipdb.set_trace()
        main_dict = dict_one.copy()
        main_dict.update(dict_two)
        return main_dict

    def markdown_to_html(self, content):
        """
        Convert the read markdown to html
        """
        return Markdown().convert(content)

