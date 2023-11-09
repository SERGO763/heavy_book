import unicodedata
import string

def shave_marks(txt):
    """Удалить все диакритические знаки"""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)