import os.path

import stagger

def get_file_info(file_path):
    '''
    Reads the ID3 tag in a music file and returns a dictionary with:
    artist, album, track and title.
    If the file does not have a ID3 tag, it will return empty dictionary.
    '''
    result = {}
    try:
        tag = stagger.read_tag(file_path)
    except stagger.NoTagError:
        # No tag on file. Returns empty dictionary.
        pass
    else:
        result['artist'] = tag.artist
        result['album'] = tag.album
        result['track'] = tag.track
        result['title'] = tag.title
    finally:
        return result

def copy_music(source, target):
    '''
    Analizes, organizes and copies all music files contained in the source
    directory to the target directory.
    '''
    if not os.path.isdir(source):
        print('{source} is not a directory or the directory is not accessable'
            .format(source=source))
        return
    for root, dirs, files in os.walk(source):
        for file in files:
            get_file_info(os.path.join(root, file))
