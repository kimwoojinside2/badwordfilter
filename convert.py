BASE_CODE, CHO_CODE, JUNG_CODE, MAX_CODE = 44032, 588, 28, 55203
CHO_LIST = list('ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ')
JUNG_LIST = list('ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ')
JONG_LIST = list(' ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ')

KORS = list('ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ')
ENGS = ['r', 'R', 'rt', 's', 'sw', 'sg', 'e', 'f', 'fr', 'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'a', 'q', 'qt', 't',
        'T', 'd', 'w', 'c', 'z', 'x', 'v', 'g',
        'k', 'o', 'i', 'O', 'j', 'p', 'u', 'P', 'h', 'hk', 'ho', 'hl', 'y', 'n', 'nj', 'np', 'nl', 'b', 'm', 'ml', 'l']
KOR_ENG_TABLE = dict(zip(KORS, ENGS))

def korToEng(text):
    res = ''
    for ch in text:
        spl = split(ch)
        if spl is None:
            res += ch
        else:
            res += ''.join([v for v in spl if v != ' '])

    engKeyList = []

    for kor in res:
        engKeyList.append(ENGS[KORS.index(kor)])

    return ''.join(engKeyList)


def combine(cho, jung, jong):
    res = BASE_CODE
    res += 0 if cho == ' ' else CHO_LIST.index(cho) * CHO_CODE
    res += 0 if jung == ' ' else JUNG_LIST.index(jung) * JUNG_CODE
    res += JONG_LIST.index(jong)
    return chr(res)


def split(kor):
    code = ord(kor) - BASE_CODE
    if code < 0 or code > MAX_CODE - BASE_CODE:
        if kor == ' ': return None
        if kor in CHO_LIST: return kor, ' ', ' '
        if kor in JUNG_LIST: return ' ', kor, ' '
        if kor in JONG_LIST: return ' ', ' ', kor
        return None
    return CHO_LIST[code // CHO_CODE], JUNG_LIST[(code % CHO_CODE) // JUNG_CODE], JONG_LIST[(code % CHO_CODE) % JUNG_CODE]

f = open("badwords.txt", "r", encoding="utf-8")
badwordList = f.readlines()
f.close()

f = open("converted.txt", "w", encoding="utf-8")
for badword in badwordList:
    badword = badword.strip("\r\n")
    f.write(korToEng(badword) + "\n")
f.close()

