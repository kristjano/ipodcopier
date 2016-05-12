import os.path
import tempfile

import stagger

from .context import ipodcopier
from ipodcopier import musiccopier

def _test_copy_music_file(expected, **tag):
    with tempfile.TemporaryDirectory() as d:
        with tempfile.NamedTemporaryFile(suffix='.mp3') as f:
            if not tag or not tag['title']:
                expected = os.path.join(expected, os.path.basename(f.name))
            stagger.util.set_frames(f, tag)
            f.seek(0)
            musiccopier.copy_music_file(f.name, d)
        assert os.path.exists(os.path.join(d, expected)), expected

def test():
    _test_copy_music_file(os.path.join('Hjálmar', 'Hljóðlega af stað',
                '{track} - {title}.mp3'.format(track=str(6).zfill(2),
                        title='Kindin Einar')),
            artist='Hjálmar', album='Hljóðlega af stað',
            track=6, title='Kindin Einar')
    _test_copy_music_file(os.path.join('Unknown artist', 'Hljóðlega af stað',
                '{track} - {title}.mp3'.format(track=str(6).zfill(2),
                        title='Kindin Einar')),
            artist='', album='Hljóðlega af stað',
            track=6, title='Kindin Einar')
    _test_copy_music_file(os.path.join('Unknown artist', 'Unknown album',
                '{track} - {title}.mp3'.format(track=str(6).zfill(2),
                        title='Kindin Einar')),
            artist='', album='',
            track=6, title='Kindin Einar')
    _test_copy_music_file(os.path.join('Unknown artist', 'Unknown album',
                '{title}.mp3'.format(title='Kindin Einar')),
            artist='', album='',
            track=0, title='Kindin Einar')
    _test_copy_music_file(os.path.join('OMAM', 'Unknown album'),
            artist='OMAM', album='',
            track=0, title='')
    _test_copy_music_file(os.path.join('Unknown artist', 'Unknown album'))

if __name__ == '__main__':
    test()
