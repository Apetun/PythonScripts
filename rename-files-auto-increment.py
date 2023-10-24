'''
author: Pure Python
url: https://www.purepython.org
copyright: CC BY-NC 4.0
creation date: 22-12-2018

This script takes a folder and renames all the files
to the same name with auto increment numbers.

It keeps the extensions of each file unchanged

Great for renaming images!

No extra pip install needed.
'''
import os


class RenameFiles:
    def __init__(self, folder=None, start_nr=0):
        self.startFolder = folder
        self.startNr = start_nr

    def loop_files(self, start_folder=None, new_name=None, start_nr=0):
        if start_folder is None and self.startFolder is not None:
            start_folder = self.startFolder

        if self.startNr >= start_nr:
            start_nr = self.startNr

        for filename in os.listdir(start_folder):
            file = os.path.join(startfolder, filename)
            filename, file_extension = os.path.splitext(file)
            number = '{0:04}'.format(start_nr)
            new_filename = "{}{}".format( number, file_extension.lower())
            newfile = os.path.join(startfolder, new_filename)
            os.rename(file, newfile)
            print("Done :{}".format(filename))
            start_nr += 1


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    startfolder = os.path.join(dir_path,"negative")
    startIncNumber = 1
    
    r = RenameFiles()
    r.loop_files(startfolder,startIncNumber)