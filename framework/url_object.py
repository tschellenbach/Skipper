import urlparse
from django.core.urlresolvers import reverse, NoReverseMatch

class UrlObject(object):
    '''
    Example Usage
            config = {
              'default': ['item', {'item_id': self.id}],
              'overview': ['item', {'item_id': self.id}],
              'add_love': ['add_love', {'item_id': self.id}],
              'remove_love': ['remove_love', {'item_id': self.id}],
              'add_featured': ['add_featured', {'item_id': self.id}],
              'remove_featured': ['remove_featured', {'item_id': self.id}],
              'all_lovers': ['all_lovers', {'item_id': self.id}],
              #'add_tag': ['add_tag', {'item_id': self.id}],
        }
        return UrlObject(self, config)
        
    unicode(self.url.default)
    '''
    def __init__(self, object, config, fail_silently=False):
        self.object = object
        self.config = config
        self.fail_silently = fail_silently

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except NoReverseMatch:
            return default

    def __getitem__(self, key):
        if isinstance(self.config[key], basestring):
            return self.config[key]

        url_name, data = self.config[key]
        if isinstance(data, dict):
            cmd = {'kwargs': data}
        else:
            cmd = {'args': data}
        try:
            url = reverse(url_name, **cmd)
        except NoReverseMatch, e:
            #fail silently on reverse errors
            if not self.fail_silently:
                raise
            else:
                url = 'noreversematch'
        return url

    def __unicode__(self):
        return self['default']

    def __str__(self):
        return unicode(self).encode('ascii', 'replace')

    def __repr__(self):
        return '<Url: %s>' % self

if __name__ == '__main__':
    import doctest
    doctest.testmod()

