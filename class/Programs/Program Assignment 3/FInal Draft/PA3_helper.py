###### Helper functions provided to you. Use as-is. Do not change #######
from os      import listdir
from os.path import isfile, isdir

class Helper:

    def clean_up(self, s):
        ''' Return a version of string str in which all letters have been
        converted to lowercase and punctuation characters have been stripped
        from both ends. Inner punctuation is left untouched. '''

        punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''

        result = s.lower().strip(punctuation)

        return result


    def get_valid_filename(self, prompt):
        '''Use prompt the name of a file. If
        the file does not exist, keep asking until a valid filename is entered.
        Return the filename.'''

        while True:

            filename = input(prompt)

            if isfile(filename): break

            print("Error: Invalid filename")

        return filename


    def read_directory_name(self, prompt):
        '''Use prompt to enter the name of a directory. If
        the directory does not exist, keep asking until a valid directory
        is entered.
        '''

        while True:

            dirname = input(prompt)

            if isdir(dirname): break

            print("Error: Invalid directory")

        return dirname


    def get_files_in_directory(self, dir):
        '''Return all files in a given directory dir.
        Will through exception if dir is not a directory.
        '''
        return listdir(dir)


    def read_signature(self, filename):
        '''Read a linguistic signature from filename and return it as
        list of features. '''

        file = open(filename, 'r')

        # the first line is the author name (string)
        result = [file.readline()]

        for line in file:
            result.append(float(line.strip())) #remaining lines include float values

        return result


##=====================================================================##