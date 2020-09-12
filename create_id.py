import hashlib

def hash_string(string):
    """
    Return a SHA-256 hash of the given string
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    #title = 'Title Goes Here'
    results = hash_string(string=title)
    print('results', results, '10-character only: ', results[:10])