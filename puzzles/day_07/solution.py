import sys

with open('input.txt', 'r') as f:
    INPUT = f.read()

LINES = INPUT.split('\n')


class FileOrFolder:
    instances = []

    def __init__(self, size=0, extension='', parent=None, name=''):
        self.size = size
        self.extension = extension
        self.__class__.instances.append(self)
        self.is_file = True if size > 0 else False
        self.parent = parent
        self.name = name
        self.foldersize = 0


def parser():
    cwd = None
    list_of_dirs = []
    for line in LINES:
        if line[:4] == '$ cd':
            # start processing new folder
            nam = line[5:]
            if nam == '..':
                if cwd: cwd = cwd.parent
            elif nam == '/':
                list_of_dirs.append(FileOrFolder(size=0, extension='', parent=None, name=nam))
            else:
                # assumes 'dir x' will always be called before '$ cd x'
                cwd = [directory for directory in FileOrFolder.instances
                       if directory.name == nam and directory.parent == cwd][0]
        elif line[:4] == '$ ls':
            # i don't think we need to do anything here
            pass
        elif line[:3] == 'dir':
            # dirs
            list_of_dirs.append(FileOrFolder(size=0, extension='', parent=cwd, name=(line[4:])))
        else:
            # files
            siz = int(line.split(' ')[0])
            nam = line.split(' ')[1].split('.')[0]
            ext = ''
            if '.' in line:
                ext = line.split(' ')[1].split('.')[1]
            list_of_dirs.append(FileOrFolder(size=siz, extension=ext, parent=cwd, name=nam))
    return list_of_dirs


def sizemaker():
    folder_sizes = []

    def get_size(parent):
        for file in (file for file in FILEFOLDER if file.parent == parent):
            def write_down(thisfile):
                if thisfile.parent is not None:
                    thisfile.parent.foldersize += file.size
                    write_down(thisfile.parent)

            write_down(file)
            get_size(file)

    get_size(parent=None)               # in other words, start with outermost directory

    # PRINT DEBUG
    # for file in FILEFOLDER:
    #     print(f'file: {file.name}, size: {file.size}, foldersize: {file.foldersize}')

    folder_sizes = [folder.foldersize for folder in FILEFOLDER if folder.foldersize > 0]
    print(folder_sizes)
    return folder_sizes


def p1():
    sum_of_sizes = 0
    for item in FOLDER_SIZES:
        if item <= 100000:
            sum_of_sizes += item

    return sum_of_sizes


def p2():
    pass


if __name__ == '__main__':
    FILEFOLDER = parser()
    FOLDER_SIZES = sizemaker()
    print(p1())

    # print(f'p1: {p1(folder)}, p2: {p2()}')
