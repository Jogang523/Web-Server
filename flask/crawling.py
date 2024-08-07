import requests
from bs4 import BeautifulSoup

def nate():
    myList = []
    myList_link = []

    res=requests.get('https://news.nate.com/recent?mid=n0100')
    soup = BeautifulSoup(res.text, 'html.parser')
    lis = soup.select('#newsContents > div.postListType.noListTitle > div.postSubjectContent > div > div > a ')

    for li in lis:
        myList.append(li.select('span h2')[0].text.strip())
        myList_link.append(li['href'])

    return myList,myList_link


def today_humor():
    myList = []
    myList_link = []

    res=requests.get('https://www.todayhumor.co.kr/board/list.php?table=bestofbest')
    soup = BeautifulSoup(res.text, 'html.parser')
    lis = soup.select('body > div.whole_box > div > div > table > tbody > tr > td.subject > a')

    for li in lis:
        myList.append(li.text.strip())
        myList_link.append(li['href'])
    
    return myList,myList_link


def clien():
    myList = []
    myList_link = [] 

    res = requests.get('https://www.clien.net/service/recommend') 
    soup = BeautifulSoup(res.text, "html.parser")
    lis = soup.select('#div_content > div.recommend_underList > div > div.list_title > a.list_subject') 

    for li in lis:
        myList.append(li.text.strip())
        myList_link.append(li['href'])
    
    return myList,myList_link

nate()