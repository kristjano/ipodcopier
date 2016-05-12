import tempfile

import stagger

from .context import ipodcopier
from ipodcopier import musiccopier

def _test_get_file_info(**expected):
    with tempfile.TemporaryFile() as f:
        # Use dummy file
        if expected: # Has ID3 tag
            stagger.util.set_frames(f, expected)
        obtained = musiccopier.get_file_info(f)
    assert obtained == expected, (obtained, expected)

def test():
    _test_get_file_info() # Test case with file with no ID3 tag
    _test_get_file_info(artist='OMAM', album='', track=0, title='')
    _test_get_file_info(artist='', album='In Rainbows', track=0, title='')
    _test_get_file_info(artist='', album='', track=5, title='')
    _test_get_file_info(artist='', album='', track=0, title='Baby One More Time')
    _test_get_file_info(artist='Hjálmar', album='Hljóðlega af stað', track=6, title='Kindin Einar')

if __name__ == '__main__':
    test()
