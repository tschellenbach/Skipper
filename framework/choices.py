

class Choices(object):
    '''
    Lazy wrapper around choice tuples
    Ensure similar naming and behaviour througout static.py :)
    
    >>> ENTITY_TYPE_CHOICES = Choices((    (0, 'item'),    (1, 'shop'),))
    >>> ENTITY_TYPE_CHOICES[0]
    'item'
    >>> ENTITY_TYPE_CHOICES['shop']
    1
    >>> list(ENTITY_TYPE_CHOICES)
    [(0, 'item'), (1, 'shop')]
    '''
    def __init__(self, tuple):
        self.tuple = tuple
        self._key_dict = self._dict = False

    def __getitem__(self, key):
        if isinstance(key, basestring):
            return self.dict[key]
        elif isinstance(key, (int, long)):
            return self.key_dict[key]
        else:
            raise ValueError, 'Input needs to be a string or something numeric'

    def __iter__(self):
        return self.tuple.__iter__()

    def __unicode__(self):
        return unicode(self.tuple)

    def get(self, key, default=None):
        if key:
            try:
                return self[key]
            except KeyError:
                pass

        return default

    @property
    def dict(self):
        if self._dict == False:
            self._dict = dict((v, k) for k, v in self.tuple)
        return self._dict

    @property
    def key_dict(self):
        if self._key_dict == False:
            self._key_dict = dict(self.tuple)
        return self._key_dict


