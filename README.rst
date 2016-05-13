ipodcopier
==========
Copy music from iPod to any computer
------------------------------------
The program copies all music files from the iPod and organizes them in the
target directory. It is organized in folder for each artist, and for each
artist the albums and then the files are renamed with track number followed
by the title.

To install the packet:

    python3 setup.py install

Or run it once:

    python3 -m ipodcopier SOURCE TARGET

Where SOURCE is the iPod device and TARGET your music directory.

You can also use the packet in you own project.

    import ipodcopier

There are three functions:

ipodcopier.copy_music(source, target)

Does the same as running the packet i.e. given source and target, copies
files from target and organizes them into target directory.

ipodcopier.copy_music_file(file_path, target)

Copies specific file and organizes it into the target directory.

ipodcopier.get_file_info(file_path)

Reads the ID3 tag for given file and returns a dictionary with 'artist',
'album', 'track' and 'title'. If there is no ID3 tag it return empty
dictionary.
