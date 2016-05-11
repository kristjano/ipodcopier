import os.path

def copy_music(source, target):
    '''
    Analizes, organizes and copies all music files contained in the source
    directory to the target directory.
    '''
    if not os.path.isdir(source):
        print('{source} is not a directory or the directory is not accessable'
            .format(source=source))
        return
