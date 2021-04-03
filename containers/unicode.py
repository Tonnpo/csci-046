import unicodedata
from copy import copy


class NormalizedStr:
    '''
    By default, Python's str type stores any valid unicode string.
    This can result in unintuitive behavior.
    For example:

    >>> 'César' in 'César Chávez'
    True
    >>> 'César' in 'César Chávez'
    False
    '''

    def __init__(self, text, normal_form='NFC'):
        self.text = text
        self.normal_form = normal_form

    def __repr__(self):
        textnorm = unicodedata.normalize(self.normal_form, self.text)
        return "NormalizedStr('" + textnorm + "', '" + self.normal_form + "')"

    def __str__(self):
        return unicodedata.normalize(self.normal_form, self.text)

    def __len__(self):
        return len(unicodedata.normalize(self.normal_form, self.text))

    def __contains__(self, substr):
        sub_norm = unicodedata.normalize(self.normal_form, substr)
        text_norm = unicodedata.normalize(self.normal_form, self.text)
        return sub_norm in text_norm

    def __getitem__(self, index):
        return list(unicodedata.normalize(self.normal_form, self.text))[index]

    def lower(self):
        text_norm = copy(unicodedata.normalize(self.normal_form, self.text))
        return text_norm.lower()

    def upper(self):
        '''
        Returns a copy in the same normalized form, but upper case.
        '''
        text_norm = copy(unicodedata.normalize(self.normal_form, self.text))
        return text_norm.lower()

    def __add__(self, b):
        text_norm = unicodedata.normalize(self.normal_form, self.text)
        b_norm = unicodedata.normalize(self.normal_form, str(b))
        combined = unicodedata.normalize(self.normal_form, text_norm + b_norm)
        return NormalizedStr(combined, self.normal_form)

    def __iter__(self):
        return NormalizedIter(self.text, self.normal_form)


class NormalizedIter:
    def __init__(self, text, normal_form):
        self.text = text
        self.normal_form = normal_form
        self.i = -1

    def __next__(self):
        if self.i < \
                len(unicodedata.normalize(self.normal_form, self.text)) - 1:
            self.i += 1
            text_norm = unicodedata.normalize(self.normal_form, self.text)
            return list(text_norm)[self.i]
        else:
            raise StopIteration
