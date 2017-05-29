# This script maps sentences in arabic to keyboards' keystrokes.

arabicMap = {
    'ض':'q',    'ص':'w',
    'ث':'e',    'ق':'r',
    'ف':'t',    'غ':'y',
    'ع':'u',    'ه':'i',
    'خ':'o',    'ح':'p',
    'ج':'[',    'د':']',
    'ش':'a',    'س':'s',
    'ي':'d',    'ب':'f',
    'ل':'g',    'ا':'h',
    'ت':'j',    'ن':'k',
    'م':'l',    'ك':';',
    'ط':"'",    'ئ':'z',
    'ء':'x',    'ؤ':'c',
    'ر':'v',    'لا':'b',
    'ى':'n',    'ة':'m',
    'و':',',    'ز':'.',
    'ظ':'/',    ' ':' ',
    '^':'^',    '_':'_',
    '؟':'?',
    '.':'.'}

def MapArabicToKeyboard(msg):
    result = ""
    for letter in msg:
        result+=arabicMap[letter]
    return result
