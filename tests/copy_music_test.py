from .context import ipodcopier
from ipodcopier import musiccopier

def test():
    assert musiccopier.copy_music('', '') == None

if __name__ == '__main__':
    test()
