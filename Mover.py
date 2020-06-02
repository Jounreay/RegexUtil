import getpass as gp
from shutil import copyfile

user = gp.getpass()
homedir = r'C:\Users\%s\Desktop\CodingProjects\RegexUtil\TestFile' % user


class FileSearch:

    def __init__(self, providerid, subfolder, date):
        self.providerid = providerid
        self.subfolder = subfolder
        self.date = date

    def filemover(self):
        return copyfile('C:\\Users\\%s\\' + self.providerid + '\\' + self.subfolder + '\\' + self.date + '\\' + '.*',
                        homedir)


#provideridinput = input(int('ProviderID to copy?: '))
#subfolderinput = input(str('Subfolder to copy?: '))
#dateinput = input(int('Date to copy?: '))

#path = FileSearch(provideridinput, subfolderinput, dateinput)
#print('Found %s, copied. Done?: ' % path.filemover())
