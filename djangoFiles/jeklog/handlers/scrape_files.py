import re

class FileScraper:
    def __init__(self, regex, file_data):
        self.regex = regex
        self.file_data = file_data

    def find_in_content(self):
        """
        Find something in the content and return things accordingly
        """
        data_found = re.findall(self.regex, self.file_data)
        return data_found[0].split(':')[1].strip()

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

