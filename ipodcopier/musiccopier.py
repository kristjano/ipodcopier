import os.path
import shutil

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

def copy_music_file(file_path, target):
    '''
    Analizes, organizes and copies single music file from path to target.
    '''
    old_filename, extension = os.path.splitext(os.path.basename(file_path))
    file_info = get_file_info(file_path)
    artist = file_info['artist'] if file_info and file_info['artist'] else 'Unknown artist'
    album = file_info['album'] if file_info and file_info['album'] else 'Unknown album'
    track = file_info['track'] if file_info and file_info['track'] else 0
    title = file_info['title'] if file_info and file_info['title'] else old_filename
    os.makedirs(os.path.join(target, artist, album), exist_ok=True)
    if track:
        filename = '{track} - {title}{extension}'.format(
                        track=str(track).zfill(2),
                        title=title, extension=extension)
    else:
        filename = '{title}{extension}'.format(
                        title=title, extension=extension)
    new_path = os.path.join(target, artist, album, filename)
    shutil.copy(file_path, new_path)

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
            copy_music_file(os.path.join(root, file), target)
