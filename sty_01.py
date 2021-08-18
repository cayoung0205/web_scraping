## 브라우저 열기
import webbrowser

url='www.google.com'
webbrowser.open(url)

## 브라우저 검색
search_url='https://www.google.com/search?query='
search_word='python'
url=search_url+search_word

webbrowser.open(url)

## for문을 이용한 브라우저 열기
urls=['www.naver.com','www.google.com','www.daum.net']

for url in urls:
    webbrowser.open(url)

## for문을 이용한 브라우저 검색
search_words=['python','C++','Java']

for search_word in search_words:
    webbrowser.open_new(search_url+search_word)