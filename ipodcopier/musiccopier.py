import os.path
import shutil
import re

import stagger

def _sanitize_filename(filename):
    '''
    Removes characters, that are illegal in path, from string.
    '''
    sanitize = re.compile(r'[^-_. \w&()]')
    return sanitize.sub('_', filename)

def _organize_info(file_path):
    '''
    Analizes and organizes the ID3 data from file.
    '''
    old_filename, _ = os.path.splitext(os.path.basename(file_path))
    file_info = get_file_info(file_path)
    if file_info and file_info['artist']:
        artist = _sanitize_filename(file_info['artist'])
    else:
        artist = 'Unknown artist'
    if file_info and file_info['album']:
        album = _sanitize_filename(file_info['album'])
    else:
        album = 'Unknown album'
    if file_info and file_info['title']:
        title = _sanitize_filename(file_info['title'])
    else:
        title = old_filename
    track = file_info['track'] if file_info and file_info['track'] else 0
    return (artist, album, title, track)

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
    artist, album, title, track = _organize_info(file_path)
    _, extension = os.path.splitext(os.path.basename(file_path))
    new_dir = os.path.join(target, artist, album)
    os.makedirs(new_dir, exist_ok=True)
    if track:
        filename = '{track} - {title}{extension}'.format(
                        track=str(track).zfill(2),
                        title=title, extension=extension)
    else:
        filename = '{title}{extension}'.format(
                        title=title, extension=extension)
    new_path = os.path.join(new_dir, filename)
    if not os.path.exists(new_path):
        return shutil.copy(file_path, new_path)
    else:
        # log: file already exists, skipping
        pass

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
