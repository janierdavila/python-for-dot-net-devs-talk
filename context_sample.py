class File:
    '''
        Example of making a custom context manager by defining __enter__ and __exit__.
        Dummy example because open function provides de same.
    '''

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

#This is how you would use it
files = []
for _ in range(10000):
    with File('foo.txt', 'w') as infile:
        infile.write('foo')
        files.append(infile)