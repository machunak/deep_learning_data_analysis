#http://openhangul.com/nlp_ko2en?q=
#오픈한글 사이트에서 한글 자판을 알파벳 자판으로 바꿔주는 서비스를 사용해서
#특정 단어를 변환하는 코드
import requests
import re

def changeWord(word):
    url = 'http://openhangul.com/nlp_ko2en?q=' + word
    response = requests.get(url)
    text = response.content
    #data = json.loads(text)
    result = text.decode('utf-8')
    wordEn = re.findall(r'<img src="images/cursor.gif"><br>(.+)', result)
    print(wordEn)
    return wordEn[0]

answer = changeWord('하늘을 따라')
print(answer)