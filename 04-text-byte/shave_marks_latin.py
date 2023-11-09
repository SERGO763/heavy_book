import unicodedata
import string

def shave_marks_latin(txt):
    """Удалить все диакритические знаки для базовых символов набора latin"""
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue  # Игнорировать диакретические знаки
                      # Для базовых символов набора Latin
            keepers.append(c)
            # Если это не модифицирующий символ, значит новый базовый
            if not unicodedata.combining(c):
                latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)

single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""",  # <1>
                           """'f"*^<''""---~>""")

multi_map = str.maketrans({  # <2>
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})

multi_map.update(single_map)

def dewnize(txt):
    """Заменить символы Win1252 символами ASCII или их последовательностями"""
    return txt.translate(multi_map)

def asciize(txt):
    no_marks = shave_marks_latin(dewnize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)
