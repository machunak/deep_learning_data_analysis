import requests
import re

def getSongs(code='W0726200', page=str(1)):
    payload = {
        'S_PAGENUMBER': '1',
        'S_MB_CD': 'W0726200',
        'S_HNBA_GBN': 'I',
        'hanmb_nm': 'G-DRAGON',
        'sort_field': 'SORT_PBCTN_DAY'
    }
    payload['S_PAGENUMBER'] = page
    payload['S_MB_CD'] = code
    url = 'https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
    songList = []
    response = requests.post(url, data=payload)
    tbody = re.findall(r'<tbody>(.+?)</tbody>', response.text, re.DOTALL)
    #print(tbody[1])
    trs = re.findall(r'<tr>(.+?)</tr>', tbody[1], re.DOTALL)

    for tr in trs:
        tr = tr.replace('<br/>', ',')
    # tr = tr.replace(' <img src="/images/common/control.gif" alt="" />', '')
    # tr = tr.replace(' <img src="/images/common/control.gif"  alt="" />', '')
        tr = re.sub(r' <img .+? />','', tr)
        tds = re.findall(r'<td>(.*?)</td>', tr)
        tds[0] = tds[0].strip()
        songList.append(tds)

    if(len(songList) == 0):
        return None
    return songList
#data = re.findall(r'<tr>.+?<td>(.+?)</td>.+?</tr>', response.text, re.DOTALL)

i = 1
while(True):

    songs = getSongs('W0726200', str(i))
    if(songs == None):
        break
    for song in songs:
        print(song)
    i += 1
